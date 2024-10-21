from flask import Flask, jsonify, request
from flask_cors import CORS
from model.usuario_model import getLogin
from model.aluno_model import getAlunosPorDocente, query_aluno_dados
from model.docente_model import getDocente
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from entities import usuario

app = Flask(__name__)
CORS(app)

@app.route('/api')
def hello():
        return 'Hello World'


@app.route('/api/login', methods=['POST'])
def login():
      if not request.is_json:
            return jsonify({'erro': 'Request body must be JSON'}),400
      data = request.get_json()
      if 'email' not in data or 'senha' not in data:
            return jsonify({'error': 'Missing email or password'}),400

      email = data['email']
      senha = data['senha']
      
      usuario = getLogin(email, senha)
      print(usuario)

      if usuario:
            return jsonify({'numero_usp': usuario.nusp,
                             'email':usuario.email,
                             'nivel': usuario.nivel
                             }),200
      else:
            return jsonify({'message':'Not found'}),404
      
@app.route('/api/<nusp_docente>/alunos', methods=['GET'])
def getAlunosDocente(nusp_docente):
      try:
            docente = getDocente(nusp_docente)
            if docente is None:
                  return jsonify({"message": "Professor not found"}), 404
            
            alunos = getAlunosPorDocente(docente.nusp)
            response_data = {
                  "docente": {
                  "nusp": docente.nusp,
                  "nome": docente.nome,
                  "cargo": docente.cargo
                  },
                  "alunos": [
                  {
                        "nusp": aluno.nusp,
                        "nome": aluno.nome,
                        "email": aluno.email,
                        "data_nascimento": aluno.data_nascimento,
                        "local_nascimento": aluno.local_nascimento,
                        "nacionalidade": aluno.nacionalidade,
                        "curso": aluno.curso,
                        "link_lattes": aluno.link_lattes,
                        "data_matricula": aluno.data_matricula,
                        "data_qualificado": aluno.data_qualificado,
                        "data_proficiencia": aluno.data_proficiencia,
                        "data_limite_trabalho_final": aluno.data_limite_trabalho_final
                  }
                  for aluno in alunos
                  ]
            }
            
            return jsonify(response_data), 200
      
      except Exception as e:
        print(f"Erro ao buscar informações para {docente.nome}: {e}")
        return jsonify({"message": "Erro interno do servidor"}), 500
      

@app.route('/api/aluno/dados', methods=['POST'])
def get_aluno_dados():
    numero_usp = request.args.get('numero_usp')
    if not numero_usp:
        return jsonify({"error": "NUMERO_USP is required"}), 400

    query_result = query_aluno_dados(numero_usp)

    if not query_result:
        return jsonify({"error": "Aluno not found"}), 404

    aluno = query_result['aluno']
    parecer = query_result['parecer']
    lattes = query_result['lattes']
    relatorio_aluno = query_result['relatorio_aluno']
    disciplinas = query_result['disciplinas']

    dados = {
        "parecer": {
            "orientador": parecer['orientador'] if parecer else None,
            "aluno": parecer['aluno'] if parecer else None,
            "textoParecer": parecer['texto_parecer'] if parecer else '',
            "desempenho": parecer['desempenho'] if parecer else '',
            "ehCcp": bool(parecer['eh_ccp']) if parecer else False,
            "resultado": parecer['resultado'] if parecer else ''
        },
        "lattes": {
            "numeroUsp": lattes['numero_usp'] if lattes else None,
            "link": lattes['link'] if lattes else '',
            "dataUltimaAtualizacao": lattes['data_ultima_atualizacao'] if lattes else None
        },
        "relatorioAluno": {
            "numeroUsp": relatorio_aluno['numero_usp'] if relatorio_aluno else None,
            "resultadoAvaliacao": relatorio_aluno['resultado_avaliacao'] if relatorio_aluno else '',
            "prazoExameQualificacao": relatorio_aluno['prazo_exame_qualificacao'] if relatorio_aluno else None,
            "prazoEntregaDissertacao": relatorio_aluno['prazo_entrega_dissertacao'] if relatorio_aluno else None,
            "atividadesAcademicas": relatorio_aluno['atividades_academicas'] if relatorio_aluno else '',
            "resumoAtividades": relatorio_aluno['resumo_atividades'] if relatorio_aluno else '',
            "observacoes": relatorio_aluno['observacoes'] if relatorio_aluno else '',
            "dificuldadeOrientador": relatorio_aluno['dificuldade_orientador'] if relatorio_aluno else ''
        },
        "disciplinas": [dict(d) for d in disciplinas],
        "aluno": {
            "numeroUsp": aluno['numero_usp'],
            "nomeCompleto": aluno['nome_completo'],
            "email": aluno['email'],
            "dataNascimento": aluno['data_nascimento'],
            "localNascimento": aluno['local_nascimento'],
            "nacionalidade": aluno['nacionalidade'],
            "curso": aluno['curso'],
            "orientador": aluno['orientador'],
            "dataMatricula": aluno['data_matricula'],
            "dataQualificacao": aluno['data_qualificacao'],
            "dataProficiencia": aluno['data_proficiencia'],
            "dataLimiteTrabalhoFinal": aluno['data_limite_trabalho_final']
        }
    }

    return jsonify({"dados": dados})

@app.route('/api/send_report_email', methods=['POST'])
def send_email():
      data = request.get_json()
      sender = data['sender']
      subject = data['subject']
      recipients = data['recipients']
      message = data['message']
      deadline = data['deadline']
      link = "https://docs.google.com/forms/d/e/1FAIpQLSeawsatuMAXsM-_qjnpl8jl1optdKuf1RFqK_pv5giadxYXaw/viewform?usp=sf_link"

      from back import envia_email

      envia_email.Email.envia_email(subject, sender, recipients, deadline, link)

      return f"Email has been sent!"    
      


if __name__ == "__main__":
    app.run(debug=True)

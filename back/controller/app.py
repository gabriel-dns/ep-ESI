from flask import Flask, jsonify, request
from flask_cors import CORS
from model.usuario_model import getLogin
from model.aluno_model import getAlunosPorDocente, query_aluno_dados,query_email_alunos
from model.docente_model import getDocente, getProfessores, postDataMax, atribuir,postCadastrarUsuarios
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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
    
    print("--------------------------TESTE ---------------------------")
    print(numero_usp)

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




@app.route('/api/alunos/email', methods=['POST'])
def get_alunos_email():
    query_result = query_email_alunos()
    print(query_result)
    if not query_result:
        return jsonify({"error": "Aluno not found"}), 404
    
    return query_result

@app.route('/api/send_report_email', methods=['POST'])
def send_email():
      data = request.get_json()
      sender = "esi.code.proj@gmail.com"
      print("bate aqui")
      subject = data['subject']
      recipients = query_email_alunos()
      deadline = data['deadline']
      link = "https://docs.google.com/forms/d/e/1FAIpQLSeawsatuMAXsM-_qjnpl8jl1optdKuf1RFqK_pv5giadxYXaw/viewform?usp=sf_link"
      print(subject)
      print(recipients)
      print(deadline)

      import envia_email

      

      envia_email.Email.envia_email(subject, sender, recipients, deadline, link)  
      return jsonify(), 200
      
@app.route('/api/parecer', methods=['POST'])
def postParecer():
      if not request.is_json:
            return jsonify({'message': 'Request body must be JSON'}),400
      data = request.get_json()
      if 'orientador' not in data:
            return jsonify({'message': 'Bad Request. The field "orientador" is requerid'}),400
      if 'aluno' not in data:
            return jsonify({'message': 'Bad Request. The field "aluno" is requerid'}),400
      if 'justificativa' not in data:
            return jsonify({'message': 'Bad Request. The field "justificativa" is requerid'}),400
      if 'desempenho' not in data:
            return jsonify({'message': 'Bad Request. The field "desempenho" is requerid'}),400
      if 'EH_CCP' not in data:
            return jsonify({'message': 'Bad Request. The field "EH_CCP" is requerid'}),400
      if 'resultado' not in data:
            return jsonify({'message': 'Bad Request. The field "resultado" is requerid'}),400
      
      orientador = getDocente(data['orientador'])
      if orientador is None:
            return jsonify({"message": "Professor not found"}), 404
      aluno = getAluno(data['aluno'])
      if aluno is None:
            return jsonify({"message": "Student not found"}), 404
      parecer = insertParecer(data['orientador'], 
                              data['aluno'], 
                              data['justificativa'], 
                              data['desempenho'],
                              data['EH_CCP'],
                              data['resultado'])
      print(parecer)
      if parecer is True:
            return jsonify(), 200
      else:
            return jsonify(), 200


@app.route('/api/professores', methods=['GET'])
def professores():
      docentes = getProfessores()

      if docentes:
            return jsonify(docentes), 200
      else:
            return jsonify({'message':'Not found'}), 404


@app.route('/api/cadastrar/dataMaxima', methods=['POST'])
def dataMaxima():
      if not request.is_json:
            return jsonify({'erro': 'Request body must be JSON'}),400

      data = request.get_json()

      dataMX = data['deadline']
      print(dataMX)
      updateResult = postDataMax(dataMX)

      if updateResult == True:
            return jsonify({'Status': updateResult}), 200
      else:
            return jsonify({"error": updateResult}), 400





@app.route('/api/atribuir', methods=['POST'])
def atribuirOrientador():
      if not request.is_json:
            return jsonify({'erro': 'Request body must be JSON'}),400

      data = request.get_json()

      aluno = data['aluno']
      orientador = data['orientador']
      print(aluno)
      print(orientador)
      updateResult = atribuir(aluno, orientador)

      return jsonify({"result": updateResult}), 200
      return jsonify(), 200


@app.route('/api/usuarios', methods=['POST'])
def usuarios():
      if not request.is_json:
            return jsonify({'erro': 'Request body must be JSON'}),400

      data = request.get_json()

      numeroUsp = data['numerousp']
      print(numeroUsp)
      email = data['email']
      print(email)
      senha = data['senha']
      print(senha)
      nivel = data['nivel']
      print(nivel)
      updateResult = postCadastrarUsuarios(numeroUsp, email,senha,nivel)

      if updateResult == True:
            return jsonify({'Status': updateResult}), 200
      else:
            return jsonify({"error": updateResult}), 400




if __name__ == "__main__":
    app.run(debug=True)

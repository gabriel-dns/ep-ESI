from flask import Flask, jsonify, request
from model.usuario_model import getLogin
from model.aluno_model import getAlunosPorDocente
from model.docente_model import getDocente
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from entities import usuario

app = Flask(__name__)

@app.route('/api')
def hello():
        return 'Hello World'


@app.route('/api/login', methods=['GET'])
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

      
      


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from back.model.user_model import *
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from entities import user

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
      
      user = getLogin(email, senha)
      print(user)

      if user:
            return jsonify({'numero_usp': user.nusp, 'email':user.email,'nivel': user.nivel}),200
      else:
            return jsonify({'message':'Not found'}),404


@app.route('/api/professores', methods=['GET'])
def professores():
      docentes = getProfessores()

      if docentes:
            return jsonify(docentes), 200
      else:
            return jsonify({'message':'Not found'}), 404


@app.route('/api/set+max+date', methods=['POST'])
def dataMaxima():
      if not request.is_json:
            return jsonify({'erro': 'Request body must be JSON'}),400

      data = request.get_json()

      if 'dataMax' not in data:
            return jsonify({'error': "Missing 'data máxima'"}),400

      dataMX = data['dataMax']

      updateResult = postDataMax(dataMX)

      if updateResult == True:
            return jsonify({'Status': updateResult}), 200
      else:
            return jsonify({"error": updateResult}), 400


if __name__ == "__main__":
    app.run(debug=True)

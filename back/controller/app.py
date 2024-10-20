from flask import Flask, jsonify, request
from model.user_model import getLogin
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

if __name__ == "__main__":
    app.run(debug=True)
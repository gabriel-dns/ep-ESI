from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/get-data', methods=['GET'])
def get_data():
    # Acessando parâmetros de URL
    name = request.args.get('name')
    age = request.args.get('age')

    # Verificando se os parâmetros foram passados
    if not name or not age:
        return jsonify({"error": "Parâmetros ausentes"}), 400

    return jsonify({"name": name, "age": age}), 200


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import date
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

@app.route('/professor/relatorios', methods=['GET'])
def get_professor_relatorios():
    professor_numero_usp = request.args.get('numero_usp')
    if not professor_numero_usp:
        return jsonify({"error": "Professor NUMERO_USP is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    today = date.today().isoformat()

    query = """
    SELECT 
        ra.NUMERO_USP AS ID_Relatorio,
        ra.ATIVIDADES_ACADEMICAS AS Conteudo,
        ra.PRAZO_EXAME_QUALIFICACAO AS Data_Submissao,
        ra.PRAZO_ENTREGA_DISSERTACAO AS Prazo_Avaliacao,
        ra.RESULTADO_AVALIACAO AS Status,
        a.NOME_COMPLETO AS Nome_Aluno,
        a.NUMERO_USP AS Matricula_Aluno
    FROM 
        RELATORIO_ALUNO ra
    JOIN 
        ALUNO a ON ra.NUMERO_USP = a.NUMERO_USP
    JOIN 
        DOCENTE d ON a.ORIENTADOR = d.NUMERO_USP
    WHERE 
        d.NUMERO_USP = %s
        AND ra.PRAZO_EXAME_QUALIFICACAO <= %s;
    """

    cursor.execute(query, (professor_numero_usp, today))
    relatorios = cursor.fetchall()

    cursor.close()
    conn.close()

    if relatorios:
        return jsonify(relatorios)
    else:
        return jsonify({"message": "No reports found for this professor with submission date earlier than today"}), 404

if __name__ == '__main__':
    app.run(debug=True)
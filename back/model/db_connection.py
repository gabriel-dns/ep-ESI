# Model/db_connection.py
import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='POSGRADUACAO',
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

from back.model.db_connection import get_db_connection
from back.entities.user import User
import base64
from functools import wraps

def validaConnection(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        conn = get_db_connection()
        if conn is None:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return None
        return f(conn, *args, **kwargs)
    return wrapper

def getLogin(email, senha):
    conn = get_db_connection()
    if conn is None:
        return None
    
    #senhaEncoded = base64.b64encode(senha)
    try:
        cursor = conn.cursor()
        
        #query = "SELECT numero_usp, email, senha, nivel FROM usuarios WHERE email like '{}' and SENHA like '{}'".format(email,senha)
        query = "select numero_usp, email, nivel from usuarios where email = '{}' and senha = '{}'".format(email, senha)
        cursor.execute(query)
        result = cursor.fetchone()
        
        user_instance = User(nusp=result[0], email=result[1], nivel=result[2], senha=senha)
        print(f"Instância de User criada: {user_instance}")
        cursor.close()
        conn.close()
        if result:
            return user_instance
        
        if result is None:
            return None

    except Exception as e:
        print('Falha ao executar query')
        return str(e)

def getProfessores():
    conn = get_db_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        query = '''SELECT * FROM DOCENTE'''
        cursor.execute(query)

        resultRows = cursor.fetchall()

        cursor.close()
        conn.close()

        docentes = []

        if resultRows is not None:
            for row in resultRows:
                docentes.append({
                    'nusp': row[0],
                    'nome-professor': row[1]
                })

        return docentes

    except Exception as e:
        print('Falha ao executar query')
        return str(e)


def postDataMax(dataMax):
    conn = get_db_connection()
    if conn is None:
        return None

    try:
        cursor = conn.cursor()

        query = f"UPDATE ALUNO SET data_limite_trabalho_final = '{dataMax}';"
        cursor.execute(query)

        result = True if cursor.rowcount > 0 else False

        conn.commit()
        cursor.close()
        conn.close()

        return result

    except Exception as e:
        return str(e)

from model.db_connection import get_db_connection
from entities.user import User
import base64

def getLogin(email,senha):
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
        return
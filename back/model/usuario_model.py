from model.db_connection import get_db_connection
from entities.usuario import Usuario
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
        
        
        cursor.close()
        conn.close()

        if result is None:
            return None
        
        if result:
            return Usuario(nusp=result[0], email=result[1], nivel=result[2], senha=senha)

    except Exception as e:
        return e
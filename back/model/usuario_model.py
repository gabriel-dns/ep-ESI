#<<<<<<< HEAD:back/model/user_model.py
#from back.model.db_connection import get_db_connection
#from back.entities.user import User
#=======
from back.model.db_connection import get_db_connection
from back.entities.usuario import Usuario
#>>>>>>> 8fc11813b8207099db0bd3b80f75f000006d9d5d:back/model/usuario_model.py
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
        
        
        cursor.close()
        conn.close()

        if result is None:
            return None
        
        if result:
            return Usuario(nusp=result[0], email=result[1], nivel=result[2], senha=senha)

    except Exception as e:
        return str(e)


#=======
#>>>>>>> 8fc11813b8207099db0bd3b80f75f000006d9d5d:back/model/usuario_model.py

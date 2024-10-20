from model.db_connection import get_db_connection
from entities.docente import Docente

def getDocente(nusp_docente):
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = "select numero_usp, nome, cargo from docente where numero_usp = '{}'".format(nusp_docente)
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        conn.close()
        print(result)
        
        if result is None:
            return None
        
        if result:
            return Docente(nusp=result[0], nome=result[1], cargo=result[2])
    
    except Exception as e:
        return e
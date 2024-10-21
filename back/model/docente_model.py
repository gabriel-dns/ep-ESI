from back.model.db_connection import get_db_connection
from back.entities.docente import Docente

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
from model.db_connection import get_db_connection
from entities.parecer import Parecer

def insertParecer(nusp_orientador, nusp_aluno, justificativa, desempenho, eh_ccp, resultado):
    conn = get_db_connection()
    if conn is None:
        return None
    
    parecer = Parecer(
        orientador=nusp_orientador, 
        aluno=nusp_aluno, 
        justificativa=justificativa, 
        desempenho=desempenho, 
        eh_ccp=eh_ccp, 
        resultado=resultado
    )

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO PARECER (ORIENTADOR, ALUNO, TEXTO_PARECER, DESEMPENHO, EH_CCP, RESULTADO)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (parecer.orientador, parecer.aluno, parecer.justificativa, parecer.desempenho, parecer.eh_ccp, parecer.resultado))
        if cursor.rowcount > 0:
            conn.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False

    except Exception as e:
        print(f"Erro ao inserir parecer {nusp_orientador}/{nusp_aluno}: {e}")
        return False
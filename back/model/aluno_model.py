from model.db_connection import get_db_connection
from entities.aluno import Aluno
from psycopg2.extras import RealDictCursor


def getAluno(nusp_aluno):
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = "SELECT NUMERO_USP, NOME_COMPLETO, EMAIL, DATA_NASCIMENTO, LOCAL_NASCIMENTO, NACIONALIDADE, CURSO, ORIENTADOR, LINK_LATTES, DATA_MATRICULA, DATA_QUALIFICACAO, DATA_PROFICIENCIA, DATA_LIMITE_TRABALHO_FINAL  FROM ALUNO WHERE NUMERO_USP = '{}'".format(nusp_aluno)
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        print(result)

        if result is None:
            return None
        
        if result:
            Aluno(nusp=result[0], nome=result[1], email=result[2], data_nascimento=result[3], 
                  local_nascimento=result[4], nacionalidade=result[5], curso=result[6], 
                  orientador=result[7], link_lattes=result[8], data_matricula=result[9], 
                  data_qualificado=result[10], data_proficiencia=result[11], 
                  data_limite_trabalho_final=result[12])
            return Aluno

    except Exception as e:
        print(f"Erro ao buscar aluno {nusp_aluno}: {e}")
        return e

def getAlunosPorDocente(nusp_docente):
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = "SELECT NUMERO_USP, NOME_COMPLETO, EMAIL, DATA_NASCIMENTO, LOCAL_NASCIMENTO, NACIONALIDADE, CURSO, ORIENTADOR, LINK_LATTES, DATA_MATRICULA, DATA_QUALIFICACAO, DATA_PROFICIENCIA, DATA_LIMITE_TRABALHO_FINAL  FROM ALUNO WHERE ORIENTADOR = '{}'".format(nusp_docente)
        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        conn.close()
        print(result)

        if result is None:
            return None
        
        if result:
            lista_alunos = [
            Aluno(nusp=row[0], nome=row[1], email=row[2], data_nascimento=row[3], 
                  local_nascimento=row[4], nacionalidade=row[5], curso=row[6], 
                  orientador=row[7], link_lattes=row[8], data_matricula=row[9], 
                  data_qualificado=row[10], data_proficiencia=row[11], 
                  data_limite_trabalho_final=row[12]) 
            for row in result
        ]
        return lista_alunos
    
    except Exception as e:
        print(f"Erro ao buscar alunos do professor {nusp_docente}: {e}")
        return e

def query_aluno_dados(numero_usp):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        # Query for aluno data
        cursor.execute("SELECT * FROM ALUNO WHERE NUMERO_USP = %s", (numero_usp,))
        aluno = cursor.fetchone()

        if not aluno:
            return None

        # Query for parecer data
        cursor.execute("SELECT * FROM PARECER WHERE ALUNO = %s", (numero_usp,))
        parecer = cursor.fetchone()

        # Query for lattes data
        cursor.execute("SELECT * FROM LATTES WHERE NUMERO_USP = %s", (numero_usp,))
        lattes = cursor.fetchone()

        # Query for relatorio_aluno data
        cursor.execute("SELECT * FROM RELATORIO_ALUNO WHERE NUMERO_USP = %s", (numero_usp,))
        relatorio_aluno = cursor.fetchone()

        # Query for disciplinas data
        cursor.execute("SELECT * FROM DISCIPLINAS WHERE NUMERO_USP = %s", (numero_usp,))
        disciplinas = cursor.fetchall()

        return {
            "aluno": aluno,
            "parecer": parecer,
            "lattes": lattes,
            "relatorio_aluno": relatorio_aluno,
            "disciplinas": disciplinas
        }

    finally:
        cursor.close()
        conn.close()



def query_email_alunos():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        # Query for aluno data
        cursor.execute("SELECT email FROM ALUNO")
        emails = cursor.fetchall()
        return [item['email'] for item in emails]
    finally:
        cursor.close()
        conn.close()
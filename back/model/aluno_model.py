from model.db_connection import get_db_connection
from entities.aluno import Aluno

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
            print(lista_alunos)
        return lista_alunos
    
    except Exception as e:
        print(f"Erro ao buscar alunos do professor {nusp_docente}: {e}")
        return e


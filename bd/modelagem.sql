Gere o codigo sql postgres para criar o banco "POSGRADUACAO" com as seguintes tabelas:
TABELA: USUARIOS
NUMERO USP (CHAVE PRIMARIA)
EMAIL
SENHA
NIVEL(A, O, C)

TABELA: DOCENTE
NUMERO-USP (CHAVE PRIMARIA)
NOME
CARGO(CCP ou Professor)



TABELA: Aluno 
Número USP (CHAVE PRIMARIA)
Nome completo
Email
Data de nascimento
Local de nascimento
Nacionalidade
Curso (mestrado/doutorado)
Orientador (chave para DOCENTE numero-usp)
Link para o Lattes
Data de matrícula
Data  qualificação
Data proficiência
Data limite trabalho final



TABELA: CRITERIOS
CREDITOS(%)
SEMESTRE
MATRICULA-QUALIFICAÇÃO
APROVADO-QUALIFICAÇÃO
MATRICULA-PROFICIENCIA
APROVADO-PROFICIENCIA
Número USP (CHAVE PRIMARIA)


TABELA: DISCIPLINAS
NOME
NOTA
Número USP (CHAVE PRIMARIA)



TABELA: RELATORIO ALUNO
Número USP (CHAVE PRIMARIA)
resultado da avaliação (ADEQUADO, ADEQUADO COM RESSALVAS, INSATISFATÓRIO)
prazo exame de qualificação
prazo entrega dissertação
atividades-ACADEMICAS
resumo-atividades
observações
dificuldadeOrientador



TABELA: LATTES
LINK
Data da última atualização
Número USP (CHAVE PRIMARIA)



TABELA: ARTIGOS
Número USP (CHAVE PRIMARIA)
ARTIGOS-ESCRITOS
ARTIGOS-EM-AVALIAÇÃO
ARTIGOS-AVALIADOS




TABELA: PARECER
ORIENTADOR Orientador (chave para DOCENTE numero-usp)
NOME ALUNO
TEXTO-PARECER
DESEMPENHO
EH-CCP(VERDADEIRO OU FALSO)
RESULTADO





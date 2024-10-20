CREATE DATABASE POSGRADUACAO;

CREATE TABLE USUARIOS (
    NUMERO_USP BIGINT PRIMARY KEY,
    EMAIL VARCHAR(255) NOT NULL,
    SENHA VARCHAR(255) NOT NULL,
    NIVEL CHAR(1) CHECK (NIVEL IN ('A', 'O', 'C')) NOT NULL
);

CREATE TABLE DOCENTE (
    NUMERO_USP BIGINT PRIMARY KEY,
    NOME VARCHAR(255) NOT NULL,
    CARGO VARCHAR(50) CHECK (CARGO IN ('CCP', 'Professor')) NOT NULL
);

-- Tabela: ALUNO
CREATE TABLE ALUNO (
    NUMERO_USP BIGINT PRIMARY KEY,
    NOME_COMPLETO VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255) NOT NULL,
    DATA_NASCIMENTO DATE NOT NULL,
    LOCAL_NASCIMENTO VARCHAR(255) NOT NULL,
    NACIONALIDADE VARCHAR(100) NOT NULL,
    CURSO VARCHAR(50) CHECK (CURSO IN ('Mestrado', 'Doutorado')) NOT NULL,
    ORIENTADOR BIGINT REFERENCES DOCENTE(NUMERO_USP),
    LINK_LATTES VARCHAR(255),
    DATA_MATRICULA DATE NOT NULL,
    DATA_QUALIFICACAO DATE,
    DATA_PROFICIENCIA DATE,
    DATA_LIMITE_TRABALHO_FINAL DATE
);



CREATE TABLE CRITERIOS (
    NUMERO_USP BIGINT PRIMARY KEY,
    CREDITOS NUMERIC(5, 2) NOT NULL,
    SEMESTRE VARCHAR(50) NOT NULL,
    MATRICULA_QUALIFICACAO DATE,
    APROVADO_QUALIFICACAO BOOLEAN NOT NULL,
    MATRICULA_PROFICIENCIA DATE,
    APROVADO_PROFICIENCIA BOOLEAN NOT NULL
);

CREATE TABLE DISCIPLINAS (
    NUMERO_USP BIGINT PRIMARY KEY,
    NOME VARCHAR(255) NOT NULL,
    NOTA NUMERIC(3, 2) NOT NULL
);

-- Tabela: RELATORIO_ALUNO
CREATE TABLE RELATORIO_ALUNO (
    ID_RELATORIO VARCHAR(100) PRIMARY KEY,
    NUMERO_USP BIGINT NOT NULL,
    DATA_ENVIO TIMESTAMP,
    PRAZO_EXAME_QUALIFICACAO DATE,
    PRAZO_ENTREGA_DISSERTACAO DATE,
    ATIVIDADES_ACADEMICAS TEXT,
    RESUMO_ATIVIDADES TEXT,
    OBSERVACOES TEXT,
    DIFICULDADE_ORIENTADOR TEXT,
    FOREIGN KEY (NUMERO_USP) REFERENCES ALUNO(NUMERO_USP)
);

CREATE TABLE LATTES (
    NUMERO_USP BIGINT PRIMARY KEY,
    LINK VARCHAR(255) NOT NULL,
    DATA_ULTIMA_ATUALIZACAO DATE NOT NULL
);

-- Tabela: ARTIGOS
CREATE TABLE ARTIGOS (
    NUMERO_USP BIGINT PRIMARY KEY,
    ARTIGOS_ESCRITOS INT NOT NULL,
    ARTIGOS_EM_AVALIACAO INT NOT NULL,
    ARTIGOS_AVALIADOS INT NOT NULL
);

CREATE TABLE PARECER (
    ORIENTADOR BIGINT REFERENCES DOCENTE(NUMERO_USP),
    ALUNO BIGINT REFERENCES ALUNO(NUMERO_USP),
    TEXTO_PARECER TEXT NOT NULL,
    DESEMPENHO VARCHAR(255),
    EH_CCP BOOLEAN NOT NULL,
    RESULTADO VARCHAR(255),
    PRIMARY KEY (ORIENTADOR, NOME_ALUNO)
);
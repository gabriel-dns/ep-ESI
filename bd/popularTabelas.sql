-- Inserindo dados na tabela USUARIOS
INSERT INTO USUARIOS (NUMERO_USP, EMAIL, SENHA, NIVEL) VALUES
(123456, 'usuario1@usp.br', 'senha1', 'A'),
(654321, 'usuario2@usp.br', 'senha2', 'O'),
(111222, 'usuario3@usp.br', 'senha3', 'C');

-- Inserindo dados na tabela DOCENTE
INSERT INTO DOCENTE (NUMERO_USP, NOME, CARGO) VALUES
(200001, 'Prof. Dr. João Silva', 'Professor'),
(200002, 'Profa. Dra. Maria Oliveira', 'Professor'),
(200003, 'Profa. Dra. Ana Santos', 'CCP');

-- Inserindo dados na tabela ALUNO
INSERT INTO ALUNO (NUMERO_USP, NOME_COMPLETO, EMAIL, DATA_NASCIMENTO, LOCAL_NASCIMENTO, NACIONALIDADE, CURSO, ORIENTADOR, LINK_LATTES, DATA_MATRICULA, DATA_QUALIFICACAO, DATA_PROFICIENCIA, DATA_LIMITE_TRABALHO_FINAL) VALUES
(300001, 'Carlos Souza', 'carlos.souza@usp.br', '1990-05-12', 'São Paulo', 'Brasileira', 'Mestrado', 200001, 'http://lattes.carlos.com', '2020-02-15', '2022-05-10', '2021-08-10', '2023-12-15'),
(300002, 'Fernanda Lima', 'fernanda.lima@usp.br', '1992-07-22', 'Campinas', 'Brasileira', 'Doutorado', 200002, 'http://lattes.fernanda.com', '2019-03-10', '2021-06-15', '2020-09-12', '2023-11-20'),
(300003, 'Marcelo Alves', 'marcelo.alves@usp.br', '1991-01-30', 'Rio de Janeiro', 'Brasileira', 'Mestrado', 200003, 'http://lattes.marcelo.com', '2021-04-22', NULL, NULL, '2024-04-30'),
(12549866865, 'Kennedy', 'marcelo.alves@usp.br', '1991-01-30', 'Rio de Janeiro', 'Brasileira', 'Mestrado', 200003, 'http://lattes.marcelo.com', '2021-04-22', NULL, NULL, '2024-04-30');

-- Inserindo dados na tabela CRITERIOS --DEU ERRO
INSERT INTO CRITERIOS (NUMERO_USP, CREDITOS, SEMESTRE, MATRICULA_QUALIFICACAO, APROVADO_QUALIFICACAO, MATRICULA_PROFICIENCIA, APROVADO_PROFICIENCIA) VALUES
(300001, 75.0, '1º Semestre', '2024-10-15', TRUE, '2024-10-15', TRUE),
(300002, 90.0, '2º Semestre', '2024-11-15', TRUE, '2024-11-15', TRUE),
(300003, 60.0, '1º Semestre', '2024-12-15', FALSE, NULL, FALSE);

-- Inserindo dados na tabela DISCIPLINAS
INSERT INTO DISCIPLINAS (NUMERO_USP, NOME, NOTA) VALUES
(300001, 'Métodos Quantitativos', 9.0),
(300002, 'Seminários Avançados', 8.5),
(300003, 'Análise de Dados', 9.5),
(300004, 'Estatística Aplicada', 7.5);

-- Inserindo dados na tabela RELATORIO_ALUNO
INSERT INTO RELATORIO_ALUNO (NUMERO_USP, ID_RELATORIO, DATA_ENVIO, PRAZO_EXAME_QUALIFICACAO, PRAZO_ENTREGA_DISSERTACAO, ATIVIDADES_ACADEMICAS, RESUMO_ATIVIDADES, OBSERVACOES, DIFICULDADE_ORIENTADOR) VALUES
(300001, 'ASD212ASASZXCSAC' , '2022-1-2 15:10:26' ,'2022-05-10', '2023-12-15', 'Aulas, pesquisa e seminários', 'Atividades realizadas com sucesso', 'Nenhuma', 'Nenhuma'),
(300002, 'SKAPOCKAPSKQW12AZ', '2022-3-1 17:17:55' ,'2021-06-15', '2023-11-20', 'Publicação de artigos, seminários', 'Algumas dificuldades encontradas', 'Recomenda-se maior acompanhamento', 'Comunicação insuficiente'),
(300003, 'SAKOPKXZLCKPO12K' , '2022-3-27 09:13:43' ,NULL, '2024-04-30', 'Apenas atividades de campo', 'Pouca participação em seminários', 'Desempenho abaixo do esperado', 'Falta de feedback');

-- Inserindo dados na tabela LATTES
INSERT INTO LATTES (NUMERO_USP, LINK, DATA_ULTIMA_ATUALIZACAO) VALUES
(300001, 'http://lattes.carlos.com', '2023-01-15'),
(300002, 'http://lattes.fernanda.com', '2023-05-22'),
(300003, 'http://lattes.marcelo.com', '2023-03-10');

-- Inserindo dados na tabela ARTIGOS
INSERT INTO ARTIGOS (NUMERO_USP, ARTIGOS_ESCRITOS, ARTIGOS_EM_AVALIACAO, ARTIGOS_AVALIADOS) VALUES
(300001, 2, 1, 1),
(300002, 3, 2, 2),
(300003, 1, 0, 0);

-- Inserindo dados na tabela PARECER
INSERT INTO PARECER (ORIENTADOR, ALUNO, TEXTO_PARECER, DESEMPENHO, EH_CCP, RESULTADO) VALUES
(200001, 300001, 'O aluno demonstrou bom desempenho e participação ativa nas atividades.', 'Excelente', FALSE, 'Aprovado'),
(200002, 300002, 'A aluna teve bom desempenho, com ressalvas em alguns aspectos.', 'Bom', FALSE, 'Aprovado com ressalvas'),
(200003, 300003, 'O aluno teve dificuldades em cumprir com as metas estabelecidas.', 'Insuficiente', TRUE, 'Reprovado');

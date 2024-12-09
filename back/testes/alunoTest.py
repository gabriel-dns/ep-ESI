import unittest
from unittest.mock import patch, MagicMock
from entities.aluno import Aluno
from model.aluno_model import getAluno, getAlunosPorDocente, query_aluno_dados, query_email_alunos 
class TestAlunoMethods(unittest.TestCase):

    @patch('module_with_methods.get_db_connection')
    def test_getAluno_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.fetchone.return_value = [
            123456, "João Silva", "joao.silva@usp.com", "1990-01-01", "São Paulo", "Brasileiro", "Ciência da Computação", 654321, "http://lattes.br/", "2015-02-15", "2017-02-15", "2016-02-15", "2020-02-15"
        ]

        aluno = getAluno(123456)

        self.assertIsInstance(aluno, Aluno)
        self.assertEqual(aluno.nusp, 123456)
        self.assertEqual(aluno.nome, "João Silva")

    @patch('module_with_methods.get_db_connection')
    def test_getAluno_not_found(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock no result
        mock_cursor.fetchone.return_value = None

        aluno = getAluno(123456)
        self.assertIsNone(aluno)

    @patch('module_with_methods.get_db_connection')
    def test_getAlunosPorDocente_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.fetchall.return_value = [
            [123456, "João Silva", "joao.silva@usp.br", "1990-01-01", "São Paulo", "Brasileiro", "Ciência da Computação", 654321, "http://lattes.br", "2015-02-15", "2017-02-15", "2016-02-15", "2020-02-15"],
            [789012, "Maria Oliveira", "maria.oliveira@example.com", "1992-03-01", "Rio de Janeiro", "Brasileira", "Engenharia", 654321, "http://lattes.br", "2016-03-15", "2018-03-15", "2017-03-15", "2021-03-15"]
        ]

        alunos = getAlunosPorDocente(654321)

        self.assertEqual(len(alunos), 2)
        self.assertIsInstance(alunos[0], Aluno)
        self.assertEqual(alunos[0].nusp, 123456)
        self.assertEqual(alunos[1].nusp, 789012)

    @patch('module_with_methods.get_db_connection')
    def test_query_aluno_dados_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.fetchone.side_effect = [
            {"NUMERO_USP": 123456, "NOME": "João Silva"},  # Aluno
            {"ALUNO": 123456, "PARECER": "Bom"},  # Parecer
            {"NUMERO_USP": 123456, "LATTES": "http://lattes.cnpq.br/1234"},  # Lattes
            {"NUMERO_USP": 123456, "RELATORIO": "Relatório"},  # Relatorio
        ]
        mock_cursor.fetchall.return_value = [
            {"NUMERO_USP": 123456, "DISCIPLINA": "Matemática"},
            {"NUMERO_USP": 123456, "DISCIPLINA": "Física"}
        ]

        dados = query_aluno_dados(123456)

        self.assertIn("aluno", dados)
        self.assertIn("parecer", dados)
        self.assertIn("disciplinas", dados)
        self.assertEqual(dados["aluno"]["NUMERO_USP"], 123456)

    @patch('module_with_methods.get_db_connection')
    def test_query_email_alunos_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.fetchall.return_value = [
            {"email": "joao.silva@example.com"},
            {"email": "maria.oliveira@example.com"}
        ]

        emails = query_email_alunos()

        self.assertEqual(emails, ["joao.silva@example.com", "maria.oliveira@example.com"])

if __name__ == '__main__':
    unittest.main()
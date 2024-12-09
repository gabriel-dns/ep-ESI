import unittest
from unittest.mock import patch, MagicMock
from entities.docente import Docente
from model.docente_model import getDocente, getProfessores, postDataMax, postCadastrarUsuarios, atribuir 

class TestDocenteMethods(unittest.TestCase):

    @patch('module_with_methods.get_db_connection')
    def test_getDocente_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.fetchone.return_value = [123456, "Sarajane", "C"]

        docente = getDocente(123456)

        self.assertIsInstance(docente, Docente)
        self.assertEqual(docente.nusp, 123456)
        self.assertEqual(docente.nome, "Sarajane")
        self.assertEqual(docente.cargo, "C")

    @patch('module_with_methods.get_db_connection')
    def test_getDocente_not_found(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.fetchone.return_value = None

        docente = getDocente(123456)
        self.assertIsNone(docente)

    @patch('module_with_methods.get_db_connection')
    def test_getProfessores_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock
        mock_cursor.fetchall.return_value = [
            [123456, "Sarajane"],
            [789012, "Jose Ricardo"]
        ]

        professores = getProfessores()

        self.assertEqual(professores[0]['numeroUsp'], 123456)
        self.assertEqual(professores[0]['name'], "Sarajane")

    @patch('module_with_methods.get_db_connection')
    def test_postDataMax_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.rowcount = 1

        result = postDataMax("2024-12-10")

        self.assertTrue(result)

    @patch('module_with_methods.get_db_connection')
    def test_postDataMax_failure(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock data
        mock_cursor.rowcount = 0

        result = postDataMax("2024-12-10")

        self.assertFalse(result)

    @patch('module_with_methods.get_db_connection')
    def test_postCadastrarUsuarios_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.rowcount = 1

        result = postCadastrarUsuarios(123456, "teste123@usp.br", "password123", "O")

        self.assertTrue(result)

    @patch('module_with_methods.get_db_connection')
    def test_postCadastrarUsuarios_failure(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.rowcount = 0

        result = postCadastrarUsuarios(123456, "teste123@usp.br", "password123", "O")

        self.assertFalse(result)

    @patch('module_with_methods.get_db_connection')
    def test_atribuir_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock
        mock_cursor.rowcount = 1

        result = atribuir(123456, 654321)

        self.assertTrue(result)

    @patch('module_with_methods.get_db_connection')
    def test_atribuir_failure(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.rowcount = 0

        result = atribuir(123456, 654321)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

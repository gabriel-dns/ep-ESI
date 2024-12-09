import unittest
from unittest.mock import patch, MagicMock
from entities.usuario import Usuario
from model.usuario_model import getLogin 

class TestUsuarioMethods(unittest.TestCase):

    @patch('module_with_methods.get_db_connection')
    def test_getLogin_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock 
        mock_cursor.fetchone.return_value = (123456, "teste123@usp.br", "O")

        result = getLogin("email@test.com", "password123")

        self.assertIsInstance(result, Usuario)
        self.assertEqual(result.nusp, 123456)
        self.assertEqual(result.email, "teste123@usp.br")
        self.assertEqual(result.nivel, "O")
        mock_cursor.execute.assert_called_once()

    @patch('module_with_methods.get_db_connection')
    def test_getLogin_no_result(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock
        mock_cursor.fetchone.return_value = None

        result = getLogin("teste123@usp.br", "password123")

        self.assertIsNone(result)
        mock_cursor.execute.assert_called_once()


if __name__ == '__main__':
    unittest.main()

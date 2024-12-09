import unittest
from unittest.mock import patch, MagicMock
from model.db_connection import get_db_connection
from model.parecer_model import insertParecer  # Substitua pelo nome do módulo real

class TestParecerMethods(unittest.TestCase):

    @patch('module_with_methods.get_db_connection')
    def test_insertParecer_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock behavior
        mock_cursor.rowcount = 1

        result = insertParecer(123456, 654321, "Justificativa Teste", "Excelente", True, "Aprovado")

        self.assertTrue(result)
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_called_once()

    @patch('module_with_methods.get_db_connection')
    def test_insertParecer_failure(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Mock behavior
        mock_cursor.rowcount = 0

        result = insertParecer(123456, 654321, "Justificativa Teste", "Excelente", True, "Aprovado")

        self.assertFalse(result)
        mock_cursor.execute.assert_called_once()
        mock_conn.commit.assert_not_called()

    @patch('module_with_methods.get_db_connection')
    def test_insertParecer_db_connection_none(self, mock_get_db_connection):
        mock_get_db_connection.return_value = None

        result = insertParecer(123456, 654321, "Justificativa Teste", "Excelente", True, "Aprovado")

        self.assertIsNone(result)

    @patch('module_with_methods.get_db_connection')
    def test_insertParecer_exception(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Simular exceção
        mock_cursor.execute.side_effect = Exception("Erro de teste")

        result = insertParecer(123456, 654321, "Justificativa Teste", "Excelente", True, "Aprovado")

        self.assertFalse(result)
        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()

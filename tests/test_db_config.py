import unittest
from src.db_config import get_connection_string, test_connection_stub


class TestDBConfig(unittest.TestCase):

    def test_connection_string_format(self):
        """Тест формата строки подключения"""
        conn_str = get_connection_string()
        self.assertIn("DRIVER=", conn_str)
        self.assertIn("SERVER=", conn_str)
        self.assertIn("DATABASE=", conn_str)

    def test_connection_string_not_empty(self):
        """Тест непустоты строки подключения"""
        conn_str = get_connection_string()
        self.assertTrue(len(conn_str) > 0)

    def test_connection_stub_returns_true(self):
        """Тест заглушки подключения"""
        result = test_connection_stub()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

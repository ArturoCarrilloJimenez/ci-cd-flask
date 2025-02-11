import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/prueba')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Prueba 1")


if __name__ == "__main__":
    unittest.main()
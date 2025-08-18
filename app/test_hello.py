import unittest
from hello import saludo

class TestHello(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo("Jose"), "Hola, Jose!")

if __name__ == "__main__":
    unittest.main()

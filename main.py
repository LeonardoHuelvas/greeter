import unittest
from unittest.mock import patch
from datetime import datetime
from greeter import Greeter

class GreeterTest(unittest.TestCase):
    """Clase de pruebas para la clase Greeter."""

    def test_greet_basic(self):
        """Prueba básica de la función greet para un nombre simple."""
        greeter = Greeter()
        self.assertEqual(greeter.greet("Leo"), "Hola Leo")
    
    def test_greet_strip_whitespace(self):
        """Prueba que greet elimina los espacios en blanco al principio y al final del nombre."""
        greeter = Greeter()
        self.assertEqual(greeter.greet("  Leo  "), "Hola Leo")

    def test_greet_capitalize(self):
        """Prueba que greet capitaliza la primera letra del nombre."""
        greeter = Greeter()
        self.assertEqual(greeter.greet("leo"), "Hola Leo")
    
    @patch('greeter.datetime')
    def test_greet_morning(self, mock_datetime):
        """Prueba que greet devuelve 'Good morning <nombre>' entre las 06:00 y las 12:00."""
        mock_datetime.now.return_value = datetime(2023, 1, 1, 7, 0, 0)
        greeter = Greeter()
        self.assertEqual(greeter.greet("Leo"), "Good morning Leo")
    
    @patch('greeter.datetime')
    def test_greet_evening(self, mock_datetime):
        """Prueba que greet devuelve 'Good evening <nombre>' entre las 18:00 y las 22:00."""
        mock_datetime.now.return_value = datetime(2023, 1, 1, 19, 0, 0)
        greeter = Greeter()
        self.assertEqual(greeter.greet("Leo"), "Good evening Leo")
    
    @patch('greeter.datetime')
    def test_greet_night(self, mock_datetime):
        """Prueba que greet devuelve 'Good night <nombre>' entre las 22:00 y las 06:00."""
        mock_datetime.now.return_value = datetime(2023, 1, 1, 23, 0, 0)
        greeter = Greeter()
        self.assertEqual(greeter.greet("Leo"), "Good night Leo")

    @patch('builtins.print')
    def test_greet_logging(self, mock_print):
        """Prueba que greet registra en la consola cada vez que es llamado."""
        greeter = Greeter()
        greeter.greet("Leo")
        mock_print.assert_called_with("Greet called with name: Leo")

def sum(a, b):
    """
    Función que suma dos números.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: La suma de a y b.
    """
    return a + b

class SumTest(unittest.TestCase):
    """Clase de pruebas para la función sum."""

    def test_sum(self):
        """Prueba que la función sum devuelve la suma correcta."""
        self.assertEqual(sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumerosValidos(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch (
            "builtins.input",
            return_value='777'
    )
    def test_ingreso_feliz_2(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 777)

    @patch (
            "builtins.input",
            return_value='0'
    )
    def test_ingreso_cero(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 0)

    @patch (
            "builtins.input",
            return_value='1000000'
    )
    def test_ingreso_millon(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 1000000)

class TestCalculoNumerosInvalidos(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch (
            'builtins.input',
            return_value='-1'
    )
    def test_ingreso_negativo_2(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch ( 
            'builtins.input',
            return_value='-1000'
    )
    def test_ingreso_negativo_3(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()







    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'
    )
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 
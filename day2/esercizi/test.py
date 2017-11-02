import unittest
from day2.esercizi.ex1_binomiale import fattoriale, coefficienteBinomiale
from day2.esercizi.ex2_camelCase import toCamelCase, fromCamelCase
from day2.esercizi.ex3_luggageLoader import unloadingOrder


class TestBinomiale(unittest.TestCase):
    def test_fattoriale(self):
        self.assertEqual(fattoriale(13), 6227020800, 'test fattoriale con 13')
        self.assertEqual(fattoriale(0), 1, 'test fattoriale con 0')
        self.assertEqual(fattoriale(1), 1, 'test fattoriale con 1')
        self.assertEqual(fattoriale(2), 2, 'test fattoriale con 2')

    def test_fattorialeCasiParticolari(self):
        self.assertEqual(fattoriale(0), 1, 'test fattoriale con 0')
        self.assertEqual(fattoriale(1), 1, 'test fattoriale con 1')


    def test_binomiale(self):
        self.assertEqual(coefficienteBinomiale(2, 0), 1, 'test coefficiente binomiale (2,0) ')
        self.assertEqual(coefficienteBinomiale(4, 3), 4, 'test coefficiente binomiale 4,3 ')
        self.assertEqual(coefficienteBinomiale(15, 7), 6435, 'test coefficiente binomiale 15,7')


class TestCamelCase(unittest.TestCase):
    def test_toCamelCase(self):
        self.assertEqual(toCamelCase('ciao come va'), 'CiaoComeVa', 'test camel case')
        self.assertEqual(toCamelCase('prova prova prova'), 'ProvaProvaProva', 'test camel case')

    def test_fromCamelCase(self):
        self.assertEqual(fromCamelCase('NonSonoUnaStringa'), 'non sono una stringa', 'test from camel case')
        self.assertEqual(fromCamelCase('TestDiProva'), 'test di prova', 'test from camel case')

    def test_compositionTest(self):
        self.assertEqual(toCamelCase(fromCamelCase('NonSonoUnaStringa')), 'NonSonoUnaStringa', 'test composizione toCamele(fromCamel())')
        self.assertEqual(fromCamelCase(toCamelCase('test di prova')), 'test di prova', 'test composizione fromCamele(toCamel())')

class TestLuggageLoader(unittest.TestCase):
    def test_load1(self):
        self.assertEqual(unloadingOrder([1,2,3]),[1,2,3], 'test unloading order')

    def test_load2(self):
        self.assertEqual(unloadingOrder([19,20,21]),[21,19,20], 'test unloading order')

    def test_load3(self):
        self.assertEqual(unloadingOrder([40,39,38,37,36]),[36,37,38,39,40], 'test unloading order')

    def test_load3(self):
        self.assertEqual(unloadingOrder([10,11,12,13,14,15,16,17]),[17,15,16,13,14,10,11,12], 'test unloading order')

if __name__ == '__main__':
    unittest.main()
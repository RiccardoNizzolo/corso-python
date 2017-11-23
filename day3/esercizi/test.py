import unittest
import numpy as np


from day3.esercizi.ex1_numpy import createVector2,createVector1,inverseVector,decreasingDiagonal,sortedRandomNumbers


class TestEx1(unittest.TestCase):



    def test_createVector1(self):
        self.checkShape(np.arange(5,501), createVector1())



    def test_createVector2(self):
        vect = np.zeros(503)
        vect[[0, 3, 502]] = 3
        self.checkShape(vect,createVector2())


    def test_inverseVector(self):
        a=np.array([1,5,4,3])
        b=np.array([3,4,5,1])
        self.checkShape(a, inverseVector(b))

    def test_decreasingDiagonal(self):
        c1=np.array([[1]])
        c4=np.array([[4,0,0,0],[0,3,0,0],[0,0,2,0],[0,0,0,1]])
        self.checkShape(c1,decreasingDiagonal(1))
        self.checkShape(c4, decreasingDiagonal(4))

    def test_sortedRandomNumbers(self):

        self.assertTrue(not np.array_equal(sortedRandomNumbers(), sortedRandomNumbers()), 'il vettore non è generato casualmente')
        vec=sortedRandomNumbers()
        vec
        self.assertTrue(np.array_equal(vec, np.sort(vec)),
                        'il vettore non è ordinato')
        self.assertTrue(np.max(sortedRandomNumbers())<1.5, 'il vettore ha valori maggiori di 1.5')
        self.assertTrue(np.min(sortedRandomNumbers()) > 1.0, 'il vettore ha valori minori  di 1.0')



    def checkShape(self,a,b):
        self.assertEqual(type(a), type(b), 'l''oggetto prodotto non è di tipo '+str(type(a)) )
        self.assertEqual(a.shape, b.shape, 'attesa shape di '+str(a.shape)+' invece di '+str(b.shape))
        self.assertTrue(np.array_equal(a, b), 'test correttezza vettore')


if __name__ == '__main__':
    unittest.main()
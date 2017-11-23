# encoding: utf-8
import numpy as np

# è possibile creare dei vettori o matrici anche con funzioni interne a numpy:
# documentazione:  https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-creation.html

# creare un vettore da con numeri da 5 a 15:
v1=np.arange(5,16)

# creare una matrice identità 3x3:
m1=np.eye(3)

# creare un tensore di numeri casuali di dimensione 2-3-4
t1=np.random.random((2,3,4))
print(t1)

# ESERCIZIO creare una matrice 4X4 con tutte le celle contenete il valore 1
# Suggerimento: la soluzione è nella documentazione: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.array-creation.html
#-------------------------------------------------------------------------------------- your code here!!!
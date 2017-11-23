# encoding: utf-8
import numpy as np

# è possibile fare operazioni tra vettori o matrici:
# documentazione:  https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html

# le operazioni sono element - wise. Quindi sono effettuate su un elemento alla volta.
# Quando si fa un operazione tra due vettori bisogna verificare che le dimensioni siano compatibili.
# Se le dimensioni non sono compatibili si avrà un errore di BROADCASTING.

# Es è sempre possibile sommare ad una matrice un numero:
m1=np.ones([3,3])
m2=m1+ 5.5
print('somma matrice e numero')
print(m1)
print('+ 5.5 \n=')
print(m2)

# è possibile sommare o moltiplicare matrici con la stessa dimensione:
m3=m1- np.eye(3)
print('\ndifferenza matrice matrice')
print(m1)
print('-')
print(np.eye(3))
print('=')
print(m3)

# è possibile fare il prodotto tra matrici (riga-colonna) usando np.dot
# sono supportate tutte le operazioni più comuni dell algebra lineare:
# https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.linalg.html
m4=np.array([[1,2,3],[4,5,6]])
m5=np.dot(m4,m3)

print('\n prodotto tra matrici')
print(m4)
print('X')
print(m3)
print('=')
print(m5)

m6=[[1,2,3],[1,2,1],[3,4,5]]
# ESERCIZIO calcolare il determinante della matrice m6
#-------------------------------------------------------------------------------------- your code here!!!
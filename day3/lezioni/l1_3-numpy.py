# encoding: utf-8
import numpy as np

# usando reshape è possibile modificare la shape di un array:

vect=np.arange(0,25)
mat=np.reshape(vect,(5,5))
print('vettore')
print(vect)
print('\nmatrice')
print(mat)

# numpy offre anche funzioni matematiche e d'aggregazione come sum, max, min, argmax etc..:
# documentazione:  https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.math.html

# somma per riga di una matrice:

print('somma per riga')
lineSum=np.sum(mat,axis=1)
print(lineSum)

print('somma per colonna')
columnSum=np.sum(mat,axis=0)
print(columnSum)

print('somma di tutta la matrice')
totalSum=np.sum(mat)
print(totalSum)

# massimo e posizione del massimo all'interno di una matrice
mat1=np.reshape(np.array([1,3,4,7,4,3,7,0,6]),(3,3))
print('\n Massimo e posizione del massimo')
print(mat1)
print(' massimo :'+str(np.max(mat1)))
print(' indice piatto :'+str(np.argmax(mat1)))
print(' indice unraveled  '+str( np.unravel_index(mat1.argmax(), mat1.shape)))

# ESERCIZIO scrivere una funzione che calcola la somma dei primi n numeri naturali senza usare un ciclo for o while
#-------------------------------------------------------------------------------------- your code here!!!
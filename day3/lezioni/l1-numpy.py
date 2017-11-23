# encoding: utf-8

# numpy è la libreria standard per operare con vettori e matrici.
# per utilizzare numpy bisogna fare l'import:
import numpy as np


# è possibile convertire una lista in un vettore usando la funzione array:
lista=[1,2,3,4]
vettore=np.array(lista)
print(vettore)
print(type(vettore))

# allo stesso modo una lista di liste verra convertito in una  matrice:
print('\nMatrice:')
listOfLists=[[1,2],[3,4],[5,6]]
matrice=np.array(listOfLists)
print(matrice)

# per sapere le dimensioni di un vettore o una matrice usare shape:
print('\ndimensione della matrice:')
print(matrice.shape)

# come per le liste è possibile leggere o scrivere il valore di un particolare elemento usando la notazione []
print('\nedit di un vettore')
vettore[1]=100
print(vettore)
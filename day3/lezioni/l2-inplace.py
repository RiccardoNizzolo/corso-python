# encoding: utf-8
import numpy as np


vect=np.array([3,5,1])
#in python le funzioni possono essere in-place o non in-place.
# le funzioni in-place vanno a modificare l'oggetto attraverso quale le chiamo senza restituire un valore (return None)
# le funzioni non in-place non modificano l'oggetto e restituiscono un valore.

# Ad esempio la somma è sempre non in-place. infatti queste due chiamate sono equivalenti:
vectSum=np.sum(vect)
vectSumArray=vect.sum()

print('somma usando numpy: '+str(vectSum))
print('somma usando il metodo di un array: '+str(vectSumArray))


# Per migliorare le performances funzioni come sort, append, pop , insert possono chiamate in-place
# questo significa che viene modificato direttamente l'oggetto originario
sortedVector=np.sort(vect)
sortedVectorArray=vect.sort()

# DOMANDA quale tra le due chiamate della funzione sort è in-place?
# DOMANDA come è valorizzata la variabile sortedVector?
# DOMANDA come è valorizzata la variabile sortedVectorArray? perche?
#-------------------------------------------------------------------------------------- your code here!!!

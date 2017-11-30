import numpy as np

from  sklearn.metrics.pairwise import euclidean_distances
# è possibile fare operazioni tra vettori o matrici:
# documentazione:  https://docs.scipy.org/doc/numpy-1.13.0/user/basics.broadcasting.html

# le operazioni sono element - wise. Quindi sono effettuate su un elemento alla volta.
# Quando si fa un operazione tra due vettori bisogna verificare che le dimensioni siano compatibili.
# Se le dimensioni non sono compatibili si avrà un errore di BROADCASTING.

# Es somma di due vettori:
v1=np.ones([6])
v2=np.arange(0.,6.)
v3=v1+ v2


print('somma matrice e numero')
print(v1)
print('+')
print(v2)
print('=')
print(v3)

# numpy offre anche operazioni matematiche da effettuare su vettori o matrici
v4=np.power(2,v2)

print('\nEsponenziale di un vettore')
print(2)
print('**')
print(v2)
print('=')
print(v4)

# ed è possibile usare funzioni di aggregazione

print('\n somma elementi di un vettore')
somma=np.sum(v2)


print('sum(')
print(v2)
print(')\n=')
print(somma)

v5=np.ones(7)
v6=np.arange(0,7)

# ESERCIZIO creare una funzione che calcola la distanza euclidea tra due punti.  Ref: https://it.wikipedia.org/wiki/Distanza_euclidea
# Usa la formula generalizzata ad uno spazio di dimensione n
# Non usare cicli for o while
# Esempio: v5 e v6 sono vettori che vivono in uno spazio di dimensione 7. La loro distanza è 7.4833
# -------------------------------------------------------------------------------------- your code here!!!

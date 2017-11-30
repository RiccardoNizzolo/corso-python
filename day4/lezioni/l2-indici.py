import numpy as np

# questa è una lista
list=[1,2,3,4,5,6]

# questo è un vettore numpy
array=np.array([0,1,2,3,4,5,6,7,8])

print('Array originale')
print(array)

# è possibile accedere agli elementi usando la seguente notazione:
# accesso puntuale
var=array[3]
print('Accesso puntuale')
print(var)

# accesso multi elemento
var=array[1:6]
print('Accesso multi elemento')
print(var)

# accesso multi elemento con lista
var=array[[0,3,4]]
print('Accesso multi elemento con lista')
print(var)

# reverse
var=array[::-1]
print('Reverse')
print(var)

# tutti i pari
var=array[::2]
print('pari')
print(var)


# tutti i dispari
var=array[1::2]
print('dispari')
print(var)

# rotazione
var=np.roll(array,2)
print('Rotazione')
print(var)

# le stesse logiche valgono per l'assegnazione
array[4:7]=1
print('Assegnazione')
print(array)

array2=np.arange(0,100)
# ESERCIZIO cambiare il segno a tutti gli elementi con indice multiplo di 3 di array2 (senza usare un ciclo for)
# -------------------------------------------------------------------------------------- your code here!!!

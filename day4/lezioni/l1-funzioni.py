import numpy as np
# in python è possibile definire nuove funzioni usando la parola chiave def.
# è utile creare le funzioni per due motivi:
#   1- riutilizzare lo stesso codice più volte
#   2- dividere il codice in blocchi logici rendendolo più leggibile

# un esempio di definizione funzione:
# tra parentesi definisco gli input della funzione
def calcolaEstampaSomma(x,y):
    sum=x+y
    print('la somma di '+str(x)+' e '+str(y)+' é '+str(sum))
    # attraverso la parola chiave return definisco qual'è l'output della funzione
    return str(x)


# esempio di utlizzo
tot=calcolaEstampaSomma(0,0)
tot=tot+calcolaEstampaSomma(1, 2)
tot=tot+calcolaEstampaSomma(3, 6)


# DOMANDA quanto vale la variabile tot al termine dell esecuzione del codice? perchè?


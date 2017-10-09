
#questo è un import statement. Grazie a questo import possiamo utilizzare tutte le funzioni della libreria RANDOM : https://docs.python.org/3/library/random.html
import random


#I booleani possono assumere solo due valori: vero o falso
#è possibile assegnare direttamente il valore di un booleano:
bol1=True
bol2=False

#oppure è possibile usare un'espressione per l'assegnamento:
a=3
b=6
bol3= (a==b)
bol4= (a<b)

print('a è uguale a b? '+str(bol3))
print('a è minore di b? '+str(bol4))

#è possibile combinare i booleani con and, or  oppure negarli con il not.
#esempio
print('a NON è uguale a b? '+str(not bol3))
print('a è uguale a b OPPURE a è minore di b? '+str(bol3 or bol4))



c=random.randint(0, 10)
print('il valore assegnato a c è: '+str(c))


#ESERCIZIO c è generato casualmente. Stampare vero se c è compreso (estremi inclusi) tra a e b. Falso altrimenti
#-------------------------------------------------------------------------------------- your code here!!!

import random

a=5
b=6

#i booleani vengono utilizzati sopratutto negli if statement:
#negli if ricoda di usare i ':' e l'indentazione (tab oppure 4 spazi)
if (a==b):
    print('a è maggiore o uguale a b')
elif(a<=b):
    print('a è minore o uguale a b')
else:
    print('a non è ne minore ne uguale b')



x=random.randint(0, 100)
y=random.randint(0, 100)
z=random.randint(0, 100)
print('x: '+str(x)+'   y: '+str(y)+'   z: '+str(z))

#ESERCIZIO x,y,z sono generati casualemtne.Scrivere del codice che usando uno o più if stampa:
# TERNA ORDINATA se x<=y<=z
# TERNA ORDINATA AL CONTRARIO se x>=y>=z
# TERNA DISORDINATA negli altri casi
#-------------------------------------------------------------------------------------- your code here!!!

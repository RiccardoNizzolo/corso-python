#ci sono vari tipi di numeri in python:
intero=3 #questo è un int()
decimale=-4.043 #questo è un float()
complesso=5.343+ 2j #questo è un complex()


#generalmente python gestisce internamente il casting tra numeri di tipo diverso. Ad esempio:
print('somma di un complesso e di un numero intero:')
print(complesso+intero)

#Ricorda che è sempre possibile fare il cast in maniera esplicita:
complesso2=complex(intero)
print('cast a complesso di un numero intero:')
print(complesso2)


#è possibile applicare ai numeri una serie di funzioni matematiche standard. qui una lista:  https://docs.python.org/3/library/functions.html
#esempio:
print('stampa il valore assoluto:')
print(abs(decimale))


#DOMANDA-- cosa succede se sommo un decimale e un complesso? di che tipo è il risultato?
#ESERCIZIO stampare il numero decimale arrotondato alla seconda cifra decimale
#-------------------------------------------------------------------------------------- your code here!!!

print('arrotondamento alla seconda cifra decimale:')

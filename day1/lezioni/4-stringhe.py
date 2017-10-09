stringa='123456789'
reverse='987654321 numeri al contrario'

#una stringa è un vettore ordinato di caratteri.
print(stringa)

#è possibile stampare i primi n caratteri di una stringa:
print(stringa[:3])
#oppure rimuovere gli ultimi n
print(stringa[:-3])
#oppure omettere i primi n
print(stringa[3:])

#è possibile sommare le stringhe:
stringaSomma=stringa+reverse

#a volte è possibile trasformare le stringhe in numeri:
numero=int(stringa)

#è sempre possibile trasfomare un numero in stringa:
numeroComeString=str(numero)


#DOMANDA-- cosa fa la somma tra due stringhe?
#ESERCIZIO stampare la variabile stringa rimuovendo i primi due e gli ultimi 4 caratteri
#ESERCIZIO stampare la lunghezza della stringa reverse. (usare la funzione len())
#-------------------------------------------------------------------------------------- your code here!!!

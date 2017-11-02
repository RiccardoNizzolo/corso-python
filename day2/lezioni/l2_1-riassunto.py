#anche le liste hanno dei metodi che vale la pena ricordare:
# doc https://docs.python.org/3.1/tutorial/datastructures.html :
lista=[1,212,31,4,5,6,7,19,12]

#aggiunge un elemento in fondo alla lista
lista.append(8)

#legge ed elimina l'ultimo elemento della lista
poppedElement=lista.pop()


#elimina il primo elemento uguale a 12
lista.remove(12)

print(poppedElement)
#ordina la lista
lista.sort()
print(lista)

frase='Lorem ipsum dolor sit amet, nec alii aperiri ne, an sed posse oratio blandit. Brute choro dolorem et cum, ad vim tale sale, ut labitur facilis mel.'

#ESERCIZIO creare una funzione che ordina e stampa le parole della varibiable frase in ordine alfabetico decrescente
#-------------------------------------------------------------------------------------- your code here!!!

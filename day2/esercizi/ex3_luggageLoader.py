# lo scopo di questo esercizio è calcolare l'ordine di scarico delle merci da una nave
#
# Inizialmente viene fornita la lista di oggetti da caricare. Ogni oggetto è identificato da un numero che indica il suo peso:
# ex toLoad=[19,22,14,24]
# ogni oggetto viene messo in un container, il container ha una capienza di 40 unità. Se l'inserimento di un nuovo oggetto supera questa soglia viene utilizzato un nuovo container:
# Esempio:
# 19->container1 22,14-->container2  24-->container3
#
#Lo scarico dei container segue una logia LIFO (last in first out) mentre lo scarico degli oggetti all'interno del container segue una logica FIFO (first in first out)
# quindi l'oridine di scaricamento dei container sarà:
# container3-> container2->container1
#  mentre l'ordine di scaricamento finale (l'output della nostra funzione) sara:
# 24,22,14,19
#
#
#

def unloadingOrder(lista):
    return lista



if __name__ == '__main__':
    print(unloadingOrder([1,2,4]))

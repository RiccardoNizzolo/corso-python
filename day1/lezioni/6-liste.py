lista1=['uno','due','tre','quattro','cinque','sei']
lista2=['1','2','3','4','5','6','7']
lista3=[1,2,3,4,5,6,7,8]

#ES1 per le liste, come per le stringhe è possibile fare un accesso puntuale:
# !! ricorda che la numerazione parte da 0!! quindi l'indice 2 corrisponde al 3zo elemento
print('ES1 3zo elemento della lista 1 : '+lista1[2])
print('\n ES1 ultimi 3 elementi della lista 1 : '+ str(lista1[-3:]))

#ES2 è possibile creare una lista di liste:
listOflists=[lista1,lista2,lista3]
print('\nES2 lista di liste:')
print(listOflists)

#ES3 è possibile accedere un elemento chiamando due volte []_
print('\nES3 lista di liste elemento 1-3: '+listOflists[0][2])


#ES4 non c'è alcun vincolo sul contenuto delle liste, possono contenre oggeti di tipo diverso:
listaMista=[1,'due',lista1,8.0,True,False]
print('\nES4 lista di vari oggetti: '+str(listaMista))

#ES5 è possibile aggiungere un elemento con il metodo append:
lista1.append('sette')
print('\nES5 la lista 1 ora ha anche l''elemento 7!:'+str(lista1))

#ES6 è possibile modificare puntualmente  un elemento della lista:
lista1[0]='elemento modificato'
print('\nES6 ho cambiato il primo elemento della lista 1: '+str(lista1))


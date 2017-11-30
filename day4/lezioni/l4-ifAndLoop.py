parola='testo'
frase1='il testo di questa frase non ha senso'
frase2='il testo di questa frase è breve'
frase3='frase semplice'
listaFrasi=[frase1,frase2,frase3]


# in python è possibile iterare liste, stringhe e array
for frase in listaFrasi:
    print(frase)

print("\n \n --- output if -- \n ")
# in python è possibile far eseguire de codice in maniera condizionale
if parola in frase1:
    print('la parola è contenuta nella frase 1')
elif parola in frase2:
    print('la parola è contenuta nella frase 2')
elif parola in frase3:
    print('la parola è contenuta nella frase 2')
else:
    print('nessuna frase contiene la parola')


# DOMANDA perche il coodice sopra non stampa la 'la parola è contenuta nella frase 2'  ma solo 'la parola è contenuta nella frase 1'?
# ESERCIZIO riscrivere il codice in maniera corretta.
# Generalizzalo usando un loop.
# -------------------------------------------------------------------------------------- your code here!!!
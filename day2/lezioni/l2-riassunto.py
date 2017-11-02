#le stringhe offrono un sacco di metodi per la loro manipolazione

caratteriAcaso='aaaaCvdCfnCskAfasdCes'
frase='   frAsE di eSeMpIO '


# usando count è possibile contare le occorrenze:
cnt=caratteriAcaso.count('C')

#è possibile trasformare una stringa in una lista di stringhe con la funzione split
lst=frase.split(' ')

#tutto maiuscolo
print(frase.upper())

#tutto minuscolo
print(frase.lower())

#rimpiazzare parti di stringa con altre stringhe
print(frase.replace(' ',' -spazio- '))

#rimuove gli spazi all'inizio o alla fine
print(frase.strip())


#ESERCIZIO scrivere una funzione che trasformi una stinga secondo le seguenti regole:
#1) gli spazi sono sostituiti da _
#2) le vocali siano scritte in maiuscolo, le consonanti in minuscolo
#3) non ci devono essere spazi o _ all'inizio o alla fine della stringa
#-------------------------------------------------------------------------------------- your code here!!!

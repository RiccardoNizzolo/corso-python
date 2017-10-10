'''
Completare la funzione in modo che presa una stringa conti il numero di parole contenute. Il sepratore tra parole è lo spazio.
es: Stringa Di Prova --> 3
    Altra Stringa Di Prova --> 4


'''
def countWord(inputString):
    numberOfWord=0
    #-------------------------------------------------------------------------------------- your code here!!!







    #-------------------------------------------------------------------------------------- end of your code !!!
    return numberOfWord




if __name__ == '__main__':
    stringheDitest=['Prova','Uno Due Tre Quattro','Per Me Si Va Ne La Città Dolente']
    risultato=[1,4,8]

    for i in range(len(risultato)):
        if(risultato[i]==countWord(stringheDitest[i])):
            print('OK test '+str(i)+' ok')
        else:
            print('FAIL test with string -' + stringheDitest[i]+ '- counted '+str(countWord(stringheDitest[i]))+' expected '+str(risultato[i]))
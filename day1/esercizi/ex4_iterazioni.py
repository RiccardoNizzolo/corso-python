'''
Completare la funzione altenateSum(lista) in modo che restituisca la somma cambiando il segno degli elementi con INDICE dispari:
es: lista=[1,2,3] --> 1-2+3=2
lista=[1,2,3,2,1] --> 1-2+3-2+1=1
lista=[1,2,3,-2,1] --> 1-2+3+2+1=5
'''

import math

def altenateSum(lista):
    risultato=0
    #-------------------------------------------------------------------------------------- your code here!!!







    #-------------------------------------------------------------------------------------- end of your code !!!
    return risultato




if __name__ == '__main__':
    tests=[[1,2,3],[1,1,1,1,1,1],[-1,1,-1,1],[1,1,1,1,1,1,1]]
    risultato=[2,0,-4,1]

    for i in range(len(risultato)):

        if(risultato[i]==altenateSum(tests[i])):
            print('OK test '+str(i)+' ok')
        else:
            print('FAIL test with list -' + str(tests[i])+ '- got '+str(altenateSum(tests[i]))+' expected '+str(risultato[i]))
'''
Completare la funzione primeNumbers(n) in modo che restituisca una lista con i numeri primi<= n:
es: primeNumbers(5)->[2,3,5]
primeNumbers(10)->[2,3,5,7]
oss: 1 non è un numero primo.

Aiuto: Il crivello di eratostene è forse l'algoritmo più semplice da implementare: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

import math

def primeNumbers(n):
    risultato=[]
    #-------------------------------------------------------------------------------------- your code here!!!







    #-------------------------------------------------------------------------------------- end of your code !!!
    return risultato




if __name__ == '__main__':
    tests=[5,11]
    risultato=[[2,3,5],[2,3,5,7,11]]

    for i in range(len(risultato)):

        if(risultato[i]==primeNumbers(tests[i])):
            print('OK test '+str(i)+' ok')
        else:
            print('FAIL test with list -' + str(tests[i])+ '- got '+str(primeNumbers(tests[i]))+' expected '+str(risultato[i]))
'''
Completare la funzione f(n) in modo che restituisca la somma dei primi n numeri naturali:
es: n=3 --> 1+2+3=6
n=5 --> 1+2+3+4+5=15
'''

import math

def f(n):
    risultato=0
    #-------------------------------------------------------------------------------------- your code here!!!







    #-------------------------------------------------------------------------------------- end of your code !!!
    return risultato




if __name__ == '__main__':
    test=[1,2,3,4,5,100,101]
    risultato=[1,3,6,10,15,5050,5151]

    for i in range(len(risultato)):

        if(risultato[i]==f(test[i])):
            print('OK test '+str(i)+' ok')
        else:
            print('FAIL test with xyz -' + str(test[i])+ '- got '+str(f(test[i]))+' expected '+str(risultato[i]))
'''
Completare la funzione f(x,y,z) i modo che restituisca il massimo tra:
1) (x+y+z)^3
2) (ln(y)/x)^z

è possibile usare le funzioni della libreria math: https://docs.python.org/3/library/math.html
'''

import math

def f(x,y,z):
    risultato=0
    #-------------------------------------------------------------------------------------- your code here!!!




    #-------------------------------------------------------------------------------------- end of your code !!!
    return risultato




if __name__ == '__main__':
    test=[[98,1,1],[0.1,math.e,10],[0.1,math.e**2,3],[89,1,2]]
    risultato=[1000000,10000000000,8000,778688]

    for i in range(len(risultato)):
        x,y,z=test[i]
        if(risultato[i]==f(x,y,z)):
            print('OK test '+str(i)+' ok')
        else:
            print('FAIL test with xyz -' + str(test[i])+ '- got '+str(f(x,y,z))+' expected '+str(risultato[i]))
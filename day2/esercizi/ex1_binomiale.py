#lo scopo di questo esercizio è crerare un metodo che calcola il coefficiente binomiale. Il coefficiente binomiale è definito come:
# C(n;k)= n!/(k!*(n-k)!)
# il ! indica il fattoriale. Quindi n! indica il prodotto dei numeri interi positivi minori o uguali a tale n:
# ad esempio 4!=4*3*2*1=24  , 2!=2*1=1
# caso particolare 0!=1
#
#Quindi per calcolare il coefficiente binomiale di (4,2) le operazioni sono le seguenti:
#  C(4;2)= 4!/(2!*(4-2)!)= 24/(2*2)=6
#
# In questo esercizio potete modificare il codice a vostro piacimento. L'unica cosa richiesta è il mantenimento della segnatura delle funzioni:
# fattoriale(n)  e coefficienteBinomiale(n,k)

def fattoriale(n):
    return 1

def coefficienteBinomiale(n,k):
    return 1


if __name__ == '__main__':
    print(fattoriale(1))
    print(coefficienteBinomiale(1,1))
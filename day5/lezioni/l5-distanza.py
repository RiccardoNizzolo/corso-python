# encoding: utf-8
import pandas as pd

# leggo i dati
f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|',low_memory =False)



# trovare i prini n prodotti con valore più vicino a 4800g
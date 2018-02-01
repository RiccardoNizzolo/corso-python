# encoding: utf-8
import pandas as pd
import numpy as np
# leggo i dati
f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|',low_memory =False)


def distanza(x,y):
    return np.abs(x-y)

# trovare i prini n prodotti con valore più vicino a 4800g
p['distanza']=distanza(4800,p['peso'])
p.sort_values('distanza',inplace=True)
p.head(2).to_excel('test.xlsx')
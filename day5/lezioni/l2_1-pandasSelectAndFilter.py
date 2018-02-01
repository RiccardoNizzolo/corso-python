# encoding: utf-8
import pandas as pd

def distanzaEuclide(x,y):
    return x*y

# leggo i dati
f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|',low_memory =False)


print('aggiungere una colonna con il prezzo al chilo dei prodotti')
# aggiungere una colonna con il prezzo al chilo dei prodotti
# -------------------------------------------------------------------------------------- your code here!!!


a=0





print('\n\n prodotti con peso tra i 3.5 e 5 kg (estremi inclusi) ')
# trovare tutti i prodotti con peso tra i 3.5 e 5 kg (estremi inclusi)
# -------------------------------------------------------------------------------------- your code here!!!
pred=p[(p['peso']>=3500) & (p['peso']<=5000) ]
a=0
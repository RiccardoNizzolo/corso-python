import pandas as pd
import numpy as np


f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')



# in pandas è possibile trovare i valori distinti usando la funzione unique()
# es: Tutti i colori dei prodotti
product_Colors=p['colore'].unique()
print(product_Colors)

# ESERCIZIO Trova i codici dei fornitori che forniscono prodotti
# -------------------------------------------------------------------------------------- your code here!!!




# ESERCIZIO Trova il numero di colori nella tabella prodotti
# -------------------------------------------------------------------------------------- your code here!!!


import pandas as pd
import numpy as np


f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')



# in pandas è possibile filtrare sulle righe.
# es: Tutti i prodotti rossi o fatti a roma
filterdData=p[(p['colore'] == 'rosso') | (p['citta'] == 'Roma')]


# ESERCIZIO trovare tutti i prodotti con peso tra i 3.5 e 5 kg (estremi inclusi)
# -------------------------------------------------------------------------------------- your code here!!!




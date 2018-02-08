import pandas as pd
import numpy as np


f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')



# con pandas è possibile ordinare il dataframe per una o più colonne
# es: ordina df per codice prodotto e quantità e data scadenza:
pf.sort_values(['codp','qta','scadenza'], ascending=False, inplace=True)
print(pf)

# ESERCIZIO Trova i codici dei due prodotti più pesanti
# -------------------------------------------------------------------------------------- your code here!!!





# ESERCIZIO Trova i codici dei fornitori che forniscono tutti i prodotti
# Aiuto: I fornitori che forniscono tutti i prodotti sono i fornitori per i quali non esiste nessun prodotto che essi non forniscano
# -------------------------------------------------------------------------------------- your code here!!!


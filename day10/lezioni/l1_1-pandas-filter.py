import pandas as pd
import numpy as np


f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')




# si può anche usare la funzione isin per filtrare su liste
# se devi filtrare sia sulle righe che sulle colonne usa dataframe.iloc
# es: i nomi dei fornitori che forniscono p2

# prima trovo i codici dei fornitori che forniscono p2
codici_fornitori_p2=pf.loc[pf['codp']=='p2','codf']


# uso i codici nella tabella f per trovare i fornitori deisderati
fornitori_p2=f[f['codf'].isin(codici_fornitori_p2)]
print(fornitori_p2)


# ESERCIZIO Trova i nomi dei fornitori che non forniscono prodotti. (ricorda che la negazione si fa con la ~)
# -------------------------------------------------------------------------------------- your code here!!!

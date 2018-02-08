import pandas as pd
import numpy as np


f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')



# in pandas è possibile unire le informazioni di più dataframe usando merge.
# l'operazione di merge ha bisogno di una colonna comune tra i due dataset.
# es: Tutti le informazioni su i prodotti forniti
info_prodotti_forniti=pd.merge(p,pf,on='codp')
print(info_prodotti_forniti)




# ESERCIZIO Trova il nome dei fornitori che non forniscono prodotti rossi
# -------------------------------------------------------------------------------------- your code here!!!




# ESERCIZIO a Londra esiste un fornitore di viti?
# -------------------------------------------------------------------------------------- your code here!!!

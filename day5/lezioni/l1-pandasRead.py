# encoding: utf-8
import pandas as pd

# leggo il file excel e lo carico in un dataframe
f=pd.read_excel('resources/f.xlsx')

# leggo file csv e lo carico in un dataframe
p=pd.read_csv('resources/p.csv', sep=';')


# stampo le prime righe 4 righe di f
#print(f.head(4))

# stampo le ultime righe 4 righe di p
#print(p.tail(4))


# ESERCIZIO Carica il file pf.csv e verifica che ha 12 righe e 4 colonne. (per verificare la dimensione del gile usa .shape)
# -------------------------------------------------------------------------------------- your code here!!!
pf=pd.read_csv('resources/pf.csv', sep='|')
print(pf.shape)



# ESERCIZIO Salva il dataframe f in formato csv ( usa la funzione to_csv):
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
# -------------------------------------------------------------------------------------- your code here!!!
f.to_csv('pippo.csv')
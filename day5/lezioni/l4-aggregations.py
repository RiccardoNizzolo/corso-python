# encoding: utf-8
import pandas as pd

# leggo i dati

pf=pd.read_csv('resources/pf.csv', sep='|',low_memory =False)

# con pandas è possibile gestire trasformazioni complesse dei dati.
# è possibile fare aggregazioni (tabelle pivot), rolling windows
# la documentazione si trova qui: https://pandas.pydata.org/pandas-docs/stable/api.html#id5


# Esempio per ogni prodotto (codp)  calcolo:
#   -il massimo,il minimo e la somma della quantità
#   -il massimo e il minimo della data di scadenza degli ordini
aggregatedDataset=pf.groupby('codp').agg({'qta': ['min', 'max','sum'], 'scadenza': ['max','min']})
print(aggregatedDataset)



# ESERCIZIO calcolare la somma della quantità in scadenza per ogni mese
# -------------------------------------------------------------------------------------- your code here!!!


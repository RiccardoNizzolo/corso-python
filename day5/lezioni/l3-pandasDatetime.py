# encoding: utf-8
import pandas as pd

# leggo i dati
f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|',low_memory =False)

# pandas offre una serie di funzioni per gestire le date

# per prima faccio il cast della colonna scadenza a datetime. In questo modo posso utilizzare le funzioni di pandas
#
pf['scadenza'] = pd.to_datetime(pf['scadenza'])

# da una data è possibile estrarre mese, ora, settimana, giorno della settimana etc ...
# documenatazione: https://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-date-components
# per esermpio stampo il giorno della settimana
print(pf['scadenza'].dt.dayofweek)



# ESERCIZIO aggiungere una colonna al dataset pf con il quarter di scadenza
# -------------------------------------------------------------------------------------- your code here!!!
print('aggiungere una colonna con il quarter di scadenza')
pf['quarter']=pf['scadenza'].dt.quarter

pf.to_excel('nome.xlsx')


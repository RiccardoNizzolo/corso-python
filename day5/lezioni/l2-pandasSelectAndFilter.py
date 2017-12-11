# encoding: utf-8
import pandas as pd

# leggo i dati
f=pd.read_excel('resources/f.xlsx')
p=pd.read_csv('resources/p.csv', sep=';')
pf=pd.read_csv('resources/pf.csv', sep='|')


# usando le [] è possibile selezionare le colonne
dat=pf[['codf','codp']]

print('\n selezione colonna \n')
print(dat)


# è possibile creare e definire nuove colonne
p['pesoKg']=p['peso']/1000

print('\n creazione nuova colonna \n')
print(p)


# è possibile creare filtri sulle righe.
# es: Tutti i prodotti rossi o fatti a roma
filterdData=p[(p['colore'] == 'rosso') | (p['citta'] == 'Roma')]

print('\n selezione righe  \n')
print(filterdData )



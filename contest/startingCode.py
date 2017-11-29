# encoding: utf-8

# import delle librerie
import pandas as pd


# carico il dataset contenente i dati di train. Modifica il path indicando dove hai salvato i file.
train = pd.read_csv('train.csv')

# carico i dati di test. Modifica il path indicando dove hai salvato i file.
test = pd.read_csv('test.csv')

# carico la submission di esempio. Modifica il path indicando dove hai salvato i file.
sampleSubmission=pd.read_csv('sampleSubmission.csv')

# Calcolo la media per ogni HouseId
aggregatedDataset=train.groupby(['HouseId']).agg({'wattConsumption':'mean'})
print('media aggregata per house id')
print(aggregatedDataset)


# aggiungo la colonna con le predizioni al dataset di test
predictions=test.merge(aggregatedDataset, left_on='HouseId',right_index=True)

# stampo le prime 5 righe del dataset
print('\n\n prime 5 righe del dataset di test con le predizioni')
print(predictions.head(5))


# Rimuovo tutte le colonne tranne id e wattConsumption
predictions=predictions[['id','wattConsumption']]

# salvo il risultato in un file di nome mySubmission.csv
predictions.to_csv('mySubmission.csv',index=False)
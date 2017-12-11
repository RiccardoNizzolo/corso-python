# encoding: utf-8
# per avere un'introduzione teorica su questo esercizio è fortemente consigliata la visione di questi 4 video:
# 1: https://www.youtube.com/watch?v=kHwlB_j7Hkc
# 2: https://www.youtube.com/watch?v=yuH4iRcggMw
# 3: https://www.youtube.com/watch?v=yR2ipCoFvNo
# 4: https://www.youtube.com/watch?v=Q4GNLhRtZNc

# Per svolgere l'esercizio è necessario essere iscritti al contest.
# Se non sei ancora iscritto segui le istrizioni nel README nella cartella contest

# ESERCIZIO
# 1) Modifica lo script per farlo funzionare con i dati del contest.
#    Verifica che l'output generato sia corretto sottomettendo il risultato (https://www.kaggle.com/c/energy-consumption/)
# 2) Modifica i parametri di inizializzazione della regressione lineare. (linea 42)
#    Cosa fanno fit_intercept e normalize? Prova a sottomettere il risultato e verifica se lo score migliora o peggiora
# 3) Prova a generare nuove features moltiplicando e/o dividendo tra loro le colonne esistenti.
#    Sottometti il risultato e verifica se la precisione delle tue previsioni migliora o peggiora
# 4) Prova ad estrarre informazione dalle features che non sono state utilizzate (datetime e idHouse).
#    Come potresti generare nuove features partendo da queste colonne?
#    prova a migliorare il tuo score includendo queste informazioni


import pandas as pd
from sklearn.linear_model import LinearRegression

# carico il dataset contenente i dati di train
train = pd.read_csv('resources\\sample_train.csv')

# carico i dati di test.
test = pd.read_csv('resources\\sample_test.csv')

# prendo dai dati di train la colonna che devo predire
label=train['wattConsumption']
# prendo la lista degli indici di test
ids=test['id']

# tengo solo le colonne che contengo misure numeriche. Elimino le features categoriche (houseId) e le date
train=train[['T_HR_AVG','SOLARAD-W/m^2','HouseId','solarPanelMq']]
test=test[['T_HR_AVG','SOLARAD-W/m^2','HouseId','solarPanelMq']]

# inizializzo la regressione lineare impostando i parametri
linear_reg=LinearRegression(fit_intercept=False, normalize=False)

# calcolo i theta della regressione lineare  usando i dati di train
linear_reg.fit(train,label)

# applico la regressione lineare ai dati di test e calcolo le previsioni
pred=linear_reg.predict(test)

# genero il file per la submission su kaggle
preds = pd.DataFrame({"id": ids, "wattConsumption": pred})
preds = preds.set_index('id')
preds.to_csv('submission.csv')

# stampo i coefficenti della regressione lineare:
theta=linear_reg.coef_
print('coefficienti Theta')
print(theta)
print('\nTheta0')
print(linear_reg.intercept_)



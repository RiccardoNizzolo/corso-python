# encoding: utf-8

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from plotly.graph_objs import *
from plotly.offline import *

def readData():
    # carico il dataset contenente i dati di train
    train = pd.read_csv('../day6/workshop/resources/train.csv')
    # cast a datetime della colonna temporale
    train['datetime'] = pd.to_datetime(train['datetime'])

    # carico i dati di test.
    test = pd.read_csv('../day6/workshop/resources/test.csv')
    # cast a datetime della colonna temporale
    test['datetime'] = pd.to_datetime(test['datetime'])

    return train, test


def trainValidationSplit(train):
    # divido i dati di train in validation-set e train-set su base temporale
    validation = train[train['datetime'] >= pd.to_datetime('2016-11-01')]
    train = train[train['datetime'] <= pd.to_datetime('2016-11-01')]

    return train, validation


def generateSubmission(test):
    test['wattConsumption']=test['prediction']
    test[['id','wattConsumption']].to_csv('submission.csv',index=False)




def plotTimeSeries(train,validation, houseId):
    # filtro i dati per HouseId
    train = train[train['HouseId'] == houseId]
    validation = validation[validation['HouseId'] == houseId]

    # genero i plot
    graps=[Scatter(x=train['datetime'],y=train['wattConsumption'],name='trainData'),
           Scatter(x=train['datetime'], y=train['prediction'], name='train Predictions'),
           Scatter(x=validation['datetime'], y=validation['wattConsumption'], name='validation Data'),
           Scatter(x=validation['datetime'], y=validation['prediction'], name='validation Predictions'),]

    # lancio il plot
    plot(graps)

if __name__ == '__main__':
    # questo scrip è identico a quello della linear regression del workshop
    # L'unica differenza è che utilizza il nearest neighbour regressor anzichè la regressione lineare
    # ESERCIZIO: verifica come performa lo script generando una submission su kaggle.
    # carico i dati
    train, test = readData()

    # ESERCIZIO ---- data transofrmation
    train['T_HR_AVG']=train['T_HR_AVG']
    test['T_HR_AVG'] = test['T_HR_AVG']
    # divido il train set in train e validation basandomi sulla data
    train, validation = trainValidationSplit(train)

    # prendo dai dati di train la colonna che devo predire
    y_train = train['wattConsumption']
    y_validation = validation['wattConsumption']


    # tengo solo le colonne che contengo misure numeriche. Elimino le date
    col2keep = ['T_HR_AVG', 'SOLARAD-W/m^2', 'solarPanelMq','HouseId']
    X_train = train[col2keep]
    X_validation = validation[col2keep]
    X_test = test[col2keep]

    # Fine parte 1 --------------------------------------------------------------------------------------------------
    # inizializzo la regressione lineare impostando i parametri
    nn = KNeighborsRegressor(n_neighbors=4)

    # calcolo i theta della regressione lineare  usando i dati di train
    nn.fit(X_train, y_train)

    # applico la regressione lineare ai dati di test, train e validation calcolando le previsioni
    test['prediction'] = nn.predict(X_test)
    validation['prediction'] = nn.predict(X_validation)
    train['prediction'] = nn.predict(X_train)

    # Fine parte 2 --------------------------------------------------------------------------------------------------
    # genero il file per la submission su kaggle
    generateSubmission(test)



    # stampo le performance su train e validation set:
    print('\n')
    print('train performace =' + str(np.sqrt(mean_squared_error(train['wattConsumption'], train['prediction']))))
    print('validation performace =' + str(np.sqrt(mean_squared_error(validation['wattConsumption'], validation['prediction']))))
    print(train['wattConsumption'].std())

    # togli il commento per visualizzare le predizioni
    #plotTimeSeries(train, validation, 3)
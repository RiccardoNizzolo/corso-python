import cufflinks as cf
import numpy as np
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    # leggo il file e lo carico in un dataframe
    train=pd.read_csv('../day6/workshop/resources/train.csv')

    train['datetime']= pd.to_datetime(train['datetime'])

    # genero una lista vuota con i plot
    plotList=[]

    # per gli houseId contenuti nel dataset
    for houseId in train['HouseId'].unique():
        # estraggo il tutti i dati relativi a quell house id
        singleHouseData=train[train['HouseId']==houseId]

        # genero il plot per la singola houseId
        #houseIdplot=go.Scatter(x=singleHouseData['datetime'],y=singleHouseData['wattConsumption'],name=str(houseId))
        houseIdplot=go.Scatter(x=singleHouseData['T_HR_AVG'],y=singleHouseData['wattConsumption'],name=str(houseId),mode='markers')

        # appendo il plot alla lista dei plot
        plotList.append(houseIdplot)


    py.plot(plotList)

    # ESERCIZIO crea uno scatter plot di temperatura vs consumo, colorato per house id.
    # Dato che non si tratta di una serie temporale dovresti disegnare punti e non linee (marker mode)
    # HINT: in questa doc è spiegato come usare la marker mode: https://plot.ly/python/line-and-scatter/
    # -------------------------------------------------------------------------------------- your code here!!!

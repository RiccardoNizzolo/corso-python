import cufflinks as cf
import numpy as np
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.linear_model import LinearRegression
from typing import List get_type_hints

from sklearn.cluster import SpectralClustering
if __name__ == '__main__':
    # leggo il file e lo carico in un dataframe
    train=pd.read_csv('../day6/workshop/resources/train.csv')

    train['datetime']= pd.to_datetime(train['datetime'])

    train=train[train['datetime']<pd.to_datetime('2016-01-20')]
    # genero una lista vuota con i plot
    plotList: List[go.Scatter] = []

    # per gli houseId contenuti nel dataset



    # genero il plot per la singola houseId
    houseIdplot=go.Scatter3d(x=train['T_HR_AVG'],y=train['SOLARAD-W/m^2'],z=train['wattConsumption'],mode='markers',marker=dict(
        size=3,
        color=train['wattConsumption'],                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    ))

    # appendo il plot alla lista dei plot
    plotList.append(houseIdplot)


    py.plot(plotList)

    # ESERCIZIO modifica lo script cambiando la colorazione dei punti in base all'house id
    # ESERCIZIO modifica la y del grafico per visualizzare il prodotto tra radiazione solare e mq di pannelli solari installati. Cosa si nota?
    # --------------------------------------------------------------------------------------

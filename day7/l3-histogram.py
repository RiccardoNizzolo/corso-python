import cufflinks as cf
import numpy as np
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objs as go

import numpy as np


if __name__ == '__main__':
    # leggo il file e lo carico in un dataframe
    train=pd.read_csv('../day6/workshop/resources/train.csv')

    train['datetime']= pd.to_datetime(train['datetime'])

    # genero una lista vuota con i plot
    plotList=[]

    train['month']=train['datetime'].dt.month

    # filtro su house id 1 in modo da prendere solo dati relativi alla prima location
    train=train[train['HouseId']==1]

    # genero l'istogramma
    histo = go.Histogram(
        x=train.loc[train['HouseId']==1,'T_HR_AVG'], name='Distribuzione Temperatura',opacity=0.75, xbins= {
            "start": -30,
            "end": 60,
            "size": 0.5
          }
    )
    # appendo l'istogramma alla lista dei plot
    plotList.append(histo)

    # generom il plot
    layout = go.Layout(barmode='overlay')
    fig = go.Figure(data=plotList, layout=layout)
    py.plot(fig, filename='stacked histogram')


    # ESERCIZIO modificare lo script. L'obbiettivio è generare 12 istogrammi sovrapposti, ognuno contenente la distribuzione della temperatura di uno specifico mese.
    # -------------------------------------------------------------------------------------- -------------------------------------------------------

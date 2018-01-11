import cufflinks as cf
from plotly.graph_objs import *
from plotly.offline import *
import pandas as pd
from sklearn.linear_model import LinearRegression



def readData():
    # carico il dataset contenente i dati di train
    train = pd.read_csv('resources/train.csv')
    train['datetime']= pd.to_datetime(train['datetime'])
    return train

def plotData(houseId,col2Plot,data):
    # creo la lista delle serie temporali che volglio disegnare
    graps=[]
    # filtro i dati per house id
    data=data[data['HouseId']==houseId]

    for col in col2Plot:
        # per ognuna delle serie che voglio disegnare aggiungo uno scatter plot
        a=Scatter(x=data['datetime'],y=data[col],name=col.lower())
        graps.append(a)
    # genero l'html con i grafici
    plot(graps)

if __name__ == '__main__':
    # leggo i dati
    train=readData()

    # seleziono le colonne che voglio plottare e l'house id
    col2Plot = ['T_HR_AVG', 'SOLARAD-kW/m^2', 'HouseId', 'solarPanelMq', 'kiloWattConsumption']
    houseid=1

    # definisco due colonne trasformando i watt in kiloWatt
    train['kiloWattConsumption']=train['wattConsumption']/1000
    train['SOLARAD-kW/m^2']=train['SOLARAD-W/m^2']/1000

    # plotto idati
    plotData(houseid,col2Plot,train)
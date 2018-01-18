# encoding: utf-8
import pandas as pd

if __name__ == '__main__':
    # leggo il file e lo carico in un dataframe
    data=pd.read_csv('../day6/workshop/resources/train.csv')

    # stampo i nomi delle colonne del dataframe
    print(data.columns)

    # stampo le statistiche sul data frame
    print(data.describe(include='all'))

    # calcolo media, massimo,minimo ed std di consumo,radiazione solare e temperatura aggregato per house id.
    houseIdAggregate=data.groupby('HouseId').agg({'wattConsumption':['max','min','mean','std'],'T_HR_AVG':['max','min','mean','std'],'SOLARAD-W/m^2':['max','min','mean','std']})
    houseIdAggregate.to_excel('output/houseIdAgg.xls')


    # ESERCIZIO Crea un file excel con la somma dei consumi aggregati per mese
    # HINT: rivedi la lezione  day5-l3 per capire come creare la colonna mese
    # -------------------------------------------------------------------------------------- your code here!!!

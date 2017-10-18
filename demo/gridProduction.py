import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import functools


def jsonFromrest(url):
    return requests.get(url).json()

def getNetgenerationSerie(serie,api_key):

    data = jsonFromrest('http://api.eia.gov/series/?'+api_key+'&series_id='+serie['series_id'])

    dataset=pd.DataFrame.from_dict(data['series'][0]['data'])
    dataset.columns = ['yyyymm', serie['name'].split(':')[2]]
    dataset.set_index(pd.to_datetime(dataset.yyyymm,format='%Y%m'),inplace=True,drop=True)
    dataset.drop('yyyymm', axis=1, inplace=True)
    return dataset


def getData():
    api_key = 'api_key=30d23a27d382eb8b24234f9dd5ed6b22'
    seriesList=jsonFromrest('http://api.eia.gov/category/?'+api_key+'&category_id=1')

    dfs = []
    for serie in seriesList['category']['childseries']:


        if (serie['name'].split(':')[4].strip()=='monthly'):
            data=getNetgenerationSerie(serie,api_key)
            dfs.append(data)

    finalDf=functools.reduce(lambda x, y: pd.merge(x, y, right_index=True,left_index=True), dfs)
    return finalDf






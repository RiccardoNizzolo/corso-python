import numpy as np
import scipy
import numpy as np
import random
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD,PCA
from sklearn.random_projection import sparse_random_matrix
import  plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import cocktails_parse_util as cp
from sklearn.cluster import SpectralClustering,KMeans


def main():
    # leggo i dati
    data = pd.read_csv('resources/cocktails_data.csv', encoding='iso-8859-1', header=None, sep='\t')

    # data transofrmation
    data['dict'] = data[data.columns[1]].astype(str).apply(get_dictionary)
    df = data['dict'].apply(pd.Series).fillna(0)
    recipes = data[data.columns[1]].astype(str).apply(cp.get_ingredientsline_grams).str.replace(',','\n')

    labels = data[data.columns[0]]
    # df['label']=labels
    df.to_csv('CData')

    # applica dimensionality reduction e fa il plot
    reduceAndPlot(df, labels, recipes)


def reduceAndPlot(data,labels,recipes):
    X_embedded=np.array(data)
    cluster=X_embedded[:,1]*0
    reduced_data=X_embedded[:,[5,7]]

    # ESERCIZIO prova questi due metodi di dimensionality reduction
    # 1) PCA http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    # 2) Tsne http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
    # ------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------

    # ESERCIZIO prova a creare una colorazione clusterizzando
    # Scegli l'algoritmo che preferisci: http://scikit-learn.org/stable/modules/clustering.html
    # ------------------------------------------------------------------------------------------


    #------------------------------------------------------------------------------------------

    plta=[]
    plta.append(go.Scatter(x=reduced_data[:, 0], y=reduced_data[:, 1] , #hovertext=np.array(recipes),
                           name='cocktails',mode='markers+text', text=labels,textposition='bottom',marker=dict(
        size=14,
        color=cluster,                # set color to an array/list of desired values
        colorscale='Jet',   # choose a colorscale
        opacity=0.8
    )))

    py.plot(plta)






def transformLine(line):
    ingredients = line.split(',')
    coctailList=''
    for ingridient in ingredients:
        ingredient = ingridient.split(':')[0]
        coctailList=coctailList+' '+ingredient


    return coctailList


def get_dictionary(line):
    ingredients = cp.get_ingredients(line)
    dict = {}
    for ingredient in ingredients:
        dict[ingredient[0]]=ingredient[1]
    return dict




if __name__ == '__main__':
    main()
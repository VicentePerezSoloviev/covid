#!/usr/bin/python
#!python

import urllib.request
from datetime import date
import pandas as pd


def dowload_dataset(urldescarga, pathdestino):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print('[', d1, ']', 'downloading dataset...')

    urllib.request.urlretrieve(urldescarga, pathdestino)

def datasetPreparement(pathdestino, pathpoblaciones):
    dt = pd.read_csv(pathdestino)

    dt['datetime'] = pd.to_datetime(dt['dateRep'], format='%d/%m/%Y')
    dt = dt.set_index('datetime')

    dt = dt.iloc[::-1]

    dt_poblaciones = pd.read_csv(pathpoblaciones)
    dt = dt.join(dt_poblaciones.set_index('Location'), on='countriesAndTerritories')

    #population is in thousands of habitants
    dt['deathsPop'] = dt['deaths'].div(dt['PopTotal']*10)
    dt['casesPop'] = dt['cases'].div(dt['PopTotal']*10)

    for i in ['cases', 'deaths', 'deathsPop', 'casesPop']:
        dt[i] = dt[i].abs()

    #dt.to_csv(pathdestino, index=True)

    return dt

def datasetCCAA(urldescarga, pathdestino):
    dowload_dataset(urldescarga, pathdestino)

    dt = pd.read_csv(pathdestino)
    del (dt['cod_ine'])

    CCAA = list(dt['CCAA'])
    fechas = list(dt.columns)[1:]
    dt_filter = pd.DataFrame(columns=['datetime'] + CCAA)
    #del (dt_filter['Total'])
    #CCAA.remove('Total')

    dt_filter['datetime'] = fechas
    dt_filter = dt_filter.set_index('datetime')

    for i in CCAA:
        datos = list(dt[dt['CCAA'] == i].values)[0][1:]
        dt_filter[i] = datos

    dt_poblaciones_ccaa = pd.read_csv(r'2915sc.csv', delimiter=';', engine='python')

    for i in CCAA:
        datos = list(dt_filter[i])
        poblacion = int(dt_poblaciones_ccaa[dt_poblaciones_ccaa['Place'] == i]['Population'])
        for j in range(1,len(datos)):
            datos[-j] = datos[-j] - datos[-j-1]
        for j in range(len(datos)):
            datos[j] = datos[j] / poblacion
        dt_filter[i] = datos

    return dt_filter

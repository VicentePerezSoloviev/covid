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

    dt['deathsPop'] = dt['deaths'].div(dt['PopTotal'])*10
    dt['casesPop'] = dt['cases'].div(dt['PopTotal'])*10

    return dt
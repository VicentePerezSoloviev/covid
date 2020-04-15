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

def datasetPreparement(pathdestino):
    dt = pd.read_csv(pathdestino)

    dt['datetime'] = pd.to_datetime(dt['dateRep'], format='%d/%m/%Y')
    dt = dt.set_index('datetime')

    dt = dt.iloc[::-1]
    return dt
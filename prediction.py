#!/usr/bin/python
#!python

from statsmodels.tsa.ar_model import AR
import pandas as pd

'''
AutoRegressive model for forecasting
'''

def prediction_AutoRegressive(pathdestino, num_predicciones):
    dt = pd.read_csv(pathdestino)

    dt['datetime'] = pd.to_datetime(dt['dateRep'], format='%d/%m/%Y')
    dt = dt.set_index('datetime')

    dt = dt.iloc[::-1]

    start_date = '03/2020'
    dt = dt[start_date:]
    dt = dt[dt['countriesAndTerritories'] == 'Spain']

    casos = list(dt['cases'].values)
    muertes = list(dt['deaths'].values)

    for i in range(num_predicciones):
        model_casos = AR(casos)
        model_muertes = AR(muertes)

        model_fit_casos = model_casos.fit()
        model_fit_muertes = model_muertes.fit()

        yhat_casos = model_fit_casos.predict(len(casos), len(casos))
        yhat_muertes = model_fit_muertes.predict(len(muertes), len(muertes))

        casos.append(int(yhat_casos))
        muertes.append(int(yhat_muertes))

    return casos[-num_predicciones:], muertes[-num_predicciones:]




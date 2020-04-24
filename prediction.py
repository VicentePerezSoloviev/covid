#!/usr/bin/python
#!python

from statsmodels.tsa.ar_model import AR
import pandas as pd

'''
AutoRegressive model for forecasting
'''

def prediction_AutoRegressive2(pathdestino, num_predicciones):
    dt = pd.read_csv(pathdestino)

    dt['datetime'] = pd.to_datetime(dt['dateRep'], format='%d/%m/%Y')
    dt = dt.set_index('datetime')

    dt = dt.iloc[::-1]

    start_date = '03/2020'
    dt = dt[start_date:]
    dt = dt[dt['countriesAndTerritories'] == 'Spain']

    casos = list(dt['cases'].values)
    muertes = list(dt['deaths'].values)

    #cases prediction

    model = AR(casos)
    model_fit = model.fit()
    window = model_fit.k_ar
    coef = model_fit.params

    print('cases prediction: window size (%d)' % window)

    history = casos[len(casos) - window:]
    history = [history[i] for i in range(len(history))]

    predictions = []
    for t in range(num_predicciones):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        predictions.append(yhat)
        history.append(yhat)

    casosPred = history[-num_predicciones:]

    # deaths prediction

    model = AR(muertes)
    model_fit = model.fit()
    window = model_fit.k_ar
    coef = model_fit.params

    print('deaths prediction: window size (%d)' %window)

    history = muertes[len(muertes) - window:]
    history = [history[i] for i in range(len(history))]

    predictions = []
    for t in range(num_predicciones):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        predictions.append(yhat)
        history.append(yhat)

    muertesPred = history[-num_predicciones:]

    return casosPred, muertesPred


def AR_model_persistence_resi_err(pathdestino, num_predicciones):
    dt = pd.read_csv(pathdestino)

    dt['datetime'] = pd.to_datetime(dt['dateRep'], format='%d/%m/%Y')
    dt = dt.set_index('datetime')

    dt = dt.iloc[::-1]

    start_date = '03/2020'
    dt = dt[start_date:]
    dt = dt[dt['countriesAndTerritories'] == 'Spain']

    casos = dt['cases']
    muertes = dt['deaths']

    casos_pred = prediction_AutoRegressive(casos, num_predicciones)
    muertes_pred = prediction_AutoRegressive(muertes, num_predicciones)

    casosPredResidual = pred_casos_residual(casos, casos_pred, num_predicciones)
    muertesPredResidual = pred_casos_residual(muertes, muertes_pred, num_predicciones)

    return casosPredResidual, muertesPredResidual


def pred_casos_residual(values, valuesPredicted, numPredicciones):
    dataframe = pd.concat([values.shift(1), values], axis=1)
    dataframe.columns = ['t-1', 't+1']
    # split into train and test sets
    X = dataframe.values[1:]
    train_X, train_y = X[:, 0], X[:, 1]
    # persistence model on training set
    train_pred = [x for x in train_X]
    # calculate residuals
    train_resid = [train_y[i] - train_pred[i] for i in range(len(train_pred))]

    model = AR(train_resid)
    model_fit = model.fit()
    window = model_fit.k_ar
    coef = model_fit.params

    history = train_resid[len(train_resid) - window:]
    history = [history[i] for i in range(len(history))]
    predictions = list()
    for t in range(numPredicciones):
        # predict error
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        pred_error = coef[0]
        for d in range(window):
            pred_error += coef[d + 1] * lag[window - d - 1]
        # correct the prediction
        yhat = valuesPredicted[t] + pred_error
        predictions.append(yhat)

    return predictions


def prediction_AutoRegressive(casos, num_predicciones):
    #cases prediction

    model = AR(casos)
    model_fit = model.fit()
    window = model_fit.k_ar
    coef = model_fit.params

    print('cases prediction: window size (%d)' % window)

    history = casos[len(casos) - window:]
    history = [history[i] for i in range(len(history))]

    predictions = []
    for t in range(num_predicciones):
        length = len(history)
        lag = [history[i] for i in range(length - window, length)]
        yhat = coef[0]
        for d in range(window):
            yhat += coef[d + 1] * lag[window - d - 1]
        predictions.append(yhat)
        history.append(yhat)

    casosPred = history[-num_predicciones:]

    return casosPred


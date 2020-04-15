#!/usr/bin/python
#!python

import numpy as np

def top_N_label(label, dataset, N):
    categorias = list(dataset['countriesAndTerritories'].value_counts().index)
    total = []
    for i in categorias:
        dt_aux = dataset[dataset['countriesAndTerritories'] == i]
        total.append([i, sum(dt_aux[label])])

    casos = [row[1] for row in total]
    paises = [row[0] for row in total]

    top_idx = np.argsort(casos)[-N:]
    top_values = [paises[i] for i in top_idx]

    return top_values

def top_N_cases(dataset, N):
    return top_N_label('cases', dataset, N)

def top_N_deaths(dataset, N):
    return top_N_label('deaths', dataset, N)

def top_perc_deaths(dataset, N):
    categorias = list(dataset['countriesAndTerritories'].value_counts().index)
    total = []
    for i in categorias:
        dt_aux = dataset[dataset['countriesAndTerritories'] == i]
        total.append([i, sum(dt_aux['deaths'])/sum(dt_aux['cases'])])

    casos = [row[1] for row in total]
    paises = [row[0] for row in total]

    top_idx = np.argsort(casos)[-N:]
    top_values1 = [paises[i] for i in top_idx]
    top_values2 = [casos[i] for i in top_idx]

    index_esp = paises.index('Spain')
    top_values1.append('Spain')
    top_values2.append(casos[index_esp])

    return top_values1, top_values2

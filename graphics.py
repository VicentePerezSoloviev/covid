#!/usr/bin/python
#!python

import matplotlib.pyplot as plt
import pandas as pd
import datetime

'''
Format ArrayCountries: countries tu print
[['ESP'], ['ITA']...]
'''
def print_death_evolution(dataset, ArrayCountries, date, fin, show = False):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'deaths', date, fin, show)

def print_cases_evolution(dataset, ArrayCountries, date, fin, show = False):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'cases', date, fin, show)

def print_label(dataset, ArrayCountries, label, date, fin, show = False):
    plt.figure(figsize=(6, 5))
    for i in ArrayCountries:
        dt_aux = dataset[dataset['countriesAndTerritories'] == i]
        dt_aux[label+'Pop'][date:fin].plot(label=i)

    plt.legend()
    if show:
        plt.show()

    plt.savefig('docs/images/' + label + '.png')
    plt.savefig('images/' + label + '.png')

def check_siglas (dataset, ArrayCountries):
    categorias = dataset['countriesAndTerritories'].value_counts()

    flag = True
    arrayFalses = []
    for i in ArrayCountries:
        if not i in categorias:
            arrayFalses.append(i)
            flag = False

    return flag, arrayFalses

def ESP_evolution(dataset, date, fin, predcasos, predmuertes, show=False):
    plt.figure(figsize=(6, 5))
    dt_aux = dataset[dataset['countriesAndTerritories'] == 'Spain'][date:fin]

    for i in range(len(predmuertes)):
        last_date = dt_aux.iloc[[-1]].index
        last_date = last_date + datetime.timedelta(days=1)

        aux = {'cases': predcasos[i], 'deaths': predmuertes[i]}
        dt_aux = dt_aux.append(pd.DataFrame(aux, index=last_date))

    dt_aux['cases'].plot(label='_nolegend_', color='green')
    dt_aux['cases'][:-len(predmuertes)].plot(label='cases', color = 'red')
    dt_aux['deaths'].plot(label='prediction', color='green')
    dt_aux['deaths'][:-len(predmuertes)].plot(label='deaths', color = 'black')

    plt.legend()
    if show:
        plt.show()

    plt.savefig('docs/images/spain.png')
    plt.savefig('images/spain.png')

def CCAA_evo (dataset, ccaa, show=False):
    plt.figure(figsize=(6, 5))
    dataset[ccaa].plot()

    plt.legend()
    if show:
        plt.show()

    plt.savefig('docs/images/ccaa.png')
    plt.savefig('images/ccaa.png')

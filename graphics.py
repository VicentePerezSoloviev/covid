#!/usr/bin/python
#!python

import matplotlib.pyplot as plt

'''
Format ArrayCountries: countries tu print
[['ESP'], ['ITA']...]
'''
def print_death_evolution(dataset, ArrayCountries, date, show = False):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'deaths', date, show)

def print_cases_evolution(dataset, ArrayCountries, date, show = False):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'cases', date, show)

def print_label(dataset, ArrayCountries, label, date, show = False):
    plt.figure(figsize=(7.5, 6))
    for i in ArrayCountries:
        dt_aux = dataset[dataset['countriesAndTerritories'] == i]
        dt_aux[label][date:].plot(label=i + ' '+ label)

    plt.legend()
    if show:
        plt.show()

    plt.savefig(label + '.png')

def check_siglas (dataset, ArrayCountries):
    categorias = dataset['countriesAndTerritories'].value_counts()

    flag = True
    arrayFalses = []
    for i in ArrayCountries:
        if not i in categorias:
            arrayFalses.append(i)
            flag = False

    return flag, arrayFalses


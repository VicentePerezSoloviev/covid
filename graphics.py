#!/usr/bin/python
#!python

import matplotlib.pyplot as plt

'''
Format ArrayCountries: countries tu print
[['ESP'], ['ITA']...]
'''
def print_death_evolution(dataset, ArrayCountries):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'deaths')

def print_cases_evolution(dataset, ArrayCountries):
    flag, array = check_siglas(dataset, ArrayCountries)
    if not flag:
        raise Exception('The following acronyms are not correct: ', array)

    print_label(dataset, ArrayCountries, 'cases')

def print_label(dataset, ArrayCountries, label):
    for i in ArrayCountries:
        dt_aux = dataset[dataset['countryterritoryCode'] == i]
        dt_aux[label].plot(figsize=(10, 8), label=i + label)

    plt.legend()
    plt.show()

def check_siglas (dataset, ArrayCountries):
    categorias = dataset['countryterritoryCode'].value_counts()

    flag = True
    arrayFalses = []
    for i in ArrayCountries:
        if not i in categorias:
            arrayFalses.append(i)
            flag = False

    return flag, arrayFalses


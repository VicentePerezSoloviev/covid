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
    plt.figure(figsize=(6, 5))
    for i in ArrayCountries:
        dt_aux = dataset[dataset['countriesAndTerritories'] == i]
        dt_aux[label+'Pop'][date:].plot(label=i)

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

def ESP_evolution(dataset, date, show=False):
    plt.figure(figsize=(6, 5))
    dt_aux = dataset[dataset['countriesAndTerritories'] == 'Spain']
    dt_aux['cases'][date:].plot(label='cases', color = 'red')
    dt_aux['deaths'][date:].plot(label='deaths', color ='black')

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

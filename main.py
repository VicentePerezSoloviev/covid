
import pandas as pd
import sys
from dataDowload import datasetPreparement, dowload_dataset
from graphics import print_cases_evolution, print_death_evolution
from stadistics import top_N_deaths, top_N_cases

#N = int(sys.argv[1])
N = 3

urlDescarga = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
pathDestino = 'dataset.csv'

dowload_dataset(urlDescarga, pathDestino)
dt = datasetPreparement(pathDestino)

top_deaths = top_N_cases(dt, N)
top_cases = top_N_deaths(dt, N)

print_death_evolution(dt, top_deaths)
print_cases_evolution(dt, top_cases)
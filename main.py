
from dataDowload import datasetPreparement, dowload_dataset
from graphics import print_cases_evolution, print_death_evolution, ESP_evolution
from stadistics import top_N_deaths, top_N_cases, top_perc_deaths
from buildHTML import generateHTML
import sys
import webbrowser

N = int(sys.argv[1])
#N = 5

urlDescarga = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
pathDestino = 'dataset.csv'

dowload_dataset(urlDescarga, pathDestino)
dt = datasetPreparement(pathDestino)

top_deaths = top_N_cases(dt, N)
top_cases = top_N_deaths(dt, N)

if 'United_States_of_America' in top_deaths:
    top_deaths.remove('United_States_of_America')
if 'United_States_of_America' in top_cases:
    top_cases.remove('United_States_of_America')

start_date = '02/2020'

print_death_evolution(dt, top_deaths, start_date)
print_cases_evolution(dt, top_cases, start_date)

countries, percentage = top_perc_deaths(dt, N*3)
generateHTML(countries, percentage)

ESP_evolution(dt, start_date)

webbrowser.open_new_tab('report.html')
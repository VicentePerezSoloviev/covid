
from dataDowload import datasetPreparement, dowload_dataset, datasetCCAA
from graphics import print_cases_evolution, print_death_evolution, ESP_evolution, CCAA_evo
from stadistics import top_N_deaths, top_N_cases, top_perc_deaths, top_N_CCAA
from buildHTML import generateHTML
from prediction import prediction_AutoRegressive2, AR_model_persistence_resi_err, SARIMA
import sys
import webbrowser
import datetime

#N = int(sys.argv[1])
N = 5

urlDescarga = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
urlDescargaCCAA = 'https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/ccaa_covid19_fallecidos.csv'
pathDestino = 'dataset.csv'
pathDestinoCCAA = 'ccaa.csv'
pathpoblaciones = 'poblaciones.csv'

dowload_dataset(urlDescarga, pathDestino)
dt = datasetPreparement(pathDestino, pathpoblaciones)

top_deaths = top_N_cases(dt, N)
top_cases = top_N_deaths(dt, N)

yesterday = datetime.datetime.now()  + datetime.timedelta(days=-1)
yesterday = yesterday.strftime("%d/%m/%Y")
start_date = '15/02/2020'

print_death_evolution(dt, top_deaths, start_date, yesterday)
print_cases_evolution(dt, top_cases, start_date, yesterday)

countries, percentage = top_perc_deaths(dt, N*3)

predcasos, predmuertes = prediction_AutoRegressive2(pathDestino, 4)
#predcasos, predmuertes = SARIMA(pathDestino, 4)
ESP_evolution(dt, '03/2020', yesterday, predcasos, predmuertes)

dt_CCAA = datasetCCAA(urlDescargaCCAA, pathDestinoCCAA)
top_ccaa = top_N_CCAA (dt_CCAA, N-2) + ['Galicia']

CCAA_evo(dt_CCAA, top_ccaa)

generateHTML(countries, percentage)

webbrowser.open_new_tab('index.html')
import math
import random
import datetime
import statistics 
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital inicial:'))
aporte = float(input('Aporte Mensal:'))
meses = int(input('prazo(meses):'))
cdi_anual = float(input('CDI anual (%)')) / 100
perc_cdb = float(input('Porcentual do CDI (%)' )) / 100
perc_lci = float(input('Porcentual do LCI (%)')) / 100
taxa_fii = float(input('rentabilidade mensal FII (%)')) / 100
meta = float(input('Meta finaceira (R$)'))

#CONVERSAO CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12)-1

#TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow ((1+taxa_cdb), meses)+ (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0,85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses)+(aporte * meses))

#poupança 
taxa_poupanca = 0.005
montante_poupaca = (capital * math.pow((1+taxa taxa_poupanca),meses)+(aporte * meses))

#FII - SIMULAÇÕES
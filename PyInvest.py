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
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci),meses)+(aporte * meses))

#poupança 
taxa_poupanca = 0.005
montante_poupaca = (capital * math.pow((1+taxa taxa_poupanca),meses)+(aporte * meses))

#FII - SIMULAÇÕES

base_fii = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))
fii1 = base_fii * (1 + random.uniform(-0.03,0.03))
fii2 = base_fii * (1 + random.uniform(-0.03,0.03))
fii3 = base_fii * (1 + random.uniform(-0.03,0.03))
fii4 = base_fii * (1 + random.uniform(-0.03,0.03))
fii5 = base_fii * (1 + random.uniform(-0.03,0.03))

# ESTATÍSTICAS
fii_media = statistics.mean([fii1,fii2,fii3,fii4,fii5])
fii_mediana = statistics.median([fii1,fii2,fii3,fii4,fii5])
fii_desvio = statistics.stdev([fii1,fii2,fii3,fii4,fii5])

# META
meta_atingida = fii_media >= meta

# DATAS
data_simulacao = datetime.datetime.now()
data_resgate = data_simulacao + datetime.timedelta(days=meses*30)

# FORMATAÇÃO MONETÁRIA
total_fmt = locale.currency(total_investido, grouping=True)
cdb_fmt = locale.currency(montante_cdb_liquido, grouping=True)
lci_fmt = locale.currency(montante_lci, grouping=True)
poup_fmt = locale.currency(montante_poupanca, grouping=True)
fii_media_fmt = locale.currency(fii_media, grouping=True)
fii_mediana_fmt = locale.currency(fii_mediana, grouping=True)
fii_desvio_fmt = locale.currency(fii_desvio, grouping=True)

# GRÁFICOS ASCII
graf_cdb = "█" * int(montante_cdb_liquido / 1000)
graf_lci = "█" * int(montante_lci / 1000)
graf_poup = "█" * int(montante_poupanca / 1000)
graf_fii = "█" * int(fii_media / 1000)

# RELATÓRIO FINAL
print("\n==============================")
print("RELATÓRIO DE SIMULAÇÃO")
print("==============================")

print("Data da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))

print("\nTotal investido:", total_fmt)

print("\n--- RESULTADOS ---")
print("CDB:", cdb_fmt)
print("LCI/LCA:", lci_fmt)
print("Poupança:", poup_fmt)
print("FII (média):", fii_media_fmt)

print("\n--- ESTATÍSTICAS DO FII ---")
print("Média:", fii_media_fmt)
print("Mediana:", fii_mediana_fmt)
print("Desvio padrão:", fii_desvio_fmt)

print("\nMeta atingida:", meta_atingida)

print("\n--- GRÁFICO DE PROJEÇÃO ---")
print("CDB     :", graf_cdb)
print("LCI/LCA :", graf_lci)
print("Poupança:", graf_poup)
print("FII     :", graf_fii)

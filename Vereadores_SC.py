# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from collections import Counter

data = pd.read_csv('Vereadores_SC.csv')
#Analise De Partido
partido = data['Partido']

Num_Partidos = Counter(partido)
Patidos_nome = Num_Partidos.keys()
Patidos_valores = Num_Partidos.values()
fig1, ax1 = plt.subplots()
ax1.pie(Patidos_valores, labels=Patidos_nome, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.show()

Candidatos_CIDADANIA = data.loc[data['Partido']=='CIDADANIA']
Candidatos_SOLIDARIEDADE = data.loc[data['Partido']=='SOLIDARIEDADE']
Candidatos_PP = data.loc[data['Partido']=='PP']
Candidatos_PDT = data.loc[data['Partido']=='PDT']
Candidatos_PTB = data.loc[data['Partido']=='PTB']
Candidatos_PSDB = data.loc[data['Partido']=='PSDB']
Candidatos_PL = data.loc[data['Partido']=='PL']
Candidatos_PT = data.loc[data['Partido']=='PT']
Candidatos_AVANTE = data.loc[data['Partido']=='AVANTE']
Candidatos_PATRIOTA = data.loc[data['Partido']=='PATRIOTA']


Mulheres_CIDADANIA = (11/len(Candidatos_CIDADANIA))*100
Mulheres_SOLIDARIEDADE = (9/len(Candidatos_SOLIDARIEDADE))*100
Mulheres_PP = (8/len(Candidatos_PP))*100
Mulheres_PDT = (7/len(Candidatos_PDT))*100
Mulheres_PTB = (9/len(Candidatos_PTB))*100
Mulheres_PSDB = (10/len(Candidatos_PSDB))*100
Mulheres_PL = (9/len(Candidatos_PL))*100
Mulheres_PT = (7/len(Candidatos_PT))*100
Mulheres_AVANTE = (5/len(Candidatos_AVANTE))*100
Mulheres_PATRIOTA = (4/len(Candidatos_PATRIOTA))*100
M_Partidos=['CIDADANIA','SOLIDARIEDADE','PP','PDT','PTB','PSDB','PL','PT','AVANTE','PATRIOTA']
Mulheres_valores=[Mulheres_CIDADANIA,Mulheres_SOLIDARIEDADE, Mulheres_PP, Mulheres_PDT, Mulheres_PTB,Mulheres_PSDB, Mulheres_PL,Mulheres_PT,Mulheres_AVANTE, Mulheres_PATRIOTA]
y_pos = np.arange(len(Patidos_nome))
plt.figure(figsize=(15,15))
plt.bar(M_Partidos, Mulheres_valores)
plt.show()


import os
import glob
import pandas as pd
#calcolare la temperatura in C (temp [K] - 273.15) 
df1 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_2mtemperature.csv")
# calcolare la pressione haPa (pressione [Pa] / 100)
df2 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_mslpressure.csv")
# calcolare la precipitazione in mm 
df3 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_totalprecipitation.csv")
df4 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_instantwindgusts.csv")
df5 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_postprocessgusts.csv")
df6 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_u10.csv")
df7 = pd.read_csv("D:/Users/sk8/Downloads/2019/19_v10.csv")

dfa1 = df1.merge(df2, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
dfa2 = dfa1.merge(df3, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
dfa3 = dfa2.merge(df4, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
dfa4 = dfa3.merge(df5, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
dfa5 = dfa4.merge(df6, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
dfa6 = dfa5.merge(df7, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])


#print(m)
dfa6.to_csv("D:/Users/sk8/Downloads/2019/2019_allparamet.csv")

#una volta esportato il file RICORDATI DI CALCOLARE wind speed (SQRT(wind_u2+windv2))  O:)


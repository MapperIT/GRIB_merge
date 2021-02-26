import os
import glob
import pandas as pd
import numpy as np

# definire il percorso dove si trovano le pale
df = pd.read_csv("D:/Work Kate/OMNINEXT/Omni-energy/MATRIX/5farm/farms.csv")

# definire il percorso della working directory (dove si trovano tutti dati)
os.chdir("D:/Work Kate/OMNINEXT/Omni-energy/MATRIX/Dati_2014-19/2019")

### carica e sistema i dati 
### temperatura
df1 = pd.read_csv("2019_2mtemperature.csv")
# calcolo della nuova colonna
df1['temperature'] = df1['value']-273.15
# pulizia delle colonne
df1 = df1.drop(columns=['Unnamed: 0','fid', 'group','value'])
# rinomina le colonne latitude e longitude
df1 = df1.rename(columns={"x": "Long", "y": "Lat"})
#print (df1)
### pressione
df2 = pd.read_csv("2019_mslpressure.csv")
df2['pressure'] = df2['value']/100
df2 = df2.drop(columns=['Unnamed: 0', 'fid', 'group', 'value'])
df2 = df2.rename(columns={"x": "Long", "y": "Lat"})
#print (df2)
### precipitation 
df3 = pd.read_csv("2019_totalprecipitation.csv")
df3['precipitation'] = df3['value']*1000
df3 = df3.drop(columns=['Unnamed: 0', 'fid', 'group', 'value'])
df3 = df3.rename(columns={"x": "Long", "y": "Lat"})
#print (df3)
### postprocessing wind gust
df4 = pd.read_csv("2019_postprocessgusts.csv")
df4 = df4.drop(columns=['Unnamed: 0', 'fid', 'group'])
df4 = df4.rename(columns={"x": "Long", "y": "Lat", "value":"postproces gust"})
#print(df4)
### instant wind gust
df5 = pd.read_csv("2019_instantwindgusts.csv")
df5 = df5.drop(columns=['Unnamed: 0', 'fid', 'group'])
df5 = df5.rename(columns={"x": "Long", "y": "Lat", "value": "instant gust"})
#print(df5)
### u 10m 
df6 = pd.read_csv("2019_u10.csv")
df6 = df6.drop(columns=['Unnamed: 0', 'fid', 'group'])
df6 = df6.rename(columns={"x": "Long", "y": "Lat", "value": "u 10"})
#print(df6)
### v 10m 
df7 = pd.read_csv("2019_v10.csv")
df7 = df7.drop(columns=['Unnamed: 0', 'fid', 'group'])
df7 = df7.rename(columns={"x": "Long", "y": "Lat", "value": "v 10"})
#print(df7)
### u 100m
df8 = pd.read_csv("2019_u100.csv")
df8 = df8.drop(columns=['Unnamed: 0', 'fid', 'group'])
df8 = df8.rename(columns={"x": "Long", "y": "Lat", "value": "u 100"})
#print(df8)
### v 100m
df9 = pd.read_csv("2019_v100.csv")
df9 = df9.drop(columns=['Unnamed: 0', 'fid', 'group'])
df9 = df9.rename(columns={"x": "Long", "y": "Lat", "value": "v 100"})
#print(df9)
### Merge dati delle pale e dati copernicus
#print (df.dtypes,df1.dtypes)
m1 = df.merge(df1, how='left', on = ['Long','Lat'])
m2 = df.merge(df2, how='left', on=['Long', 'Lat'])
m3 = df.merge(df3, how='left', on=['Long', 'Lat'])
m4 = df.merge(df4, how='left', on=['Long', 'Lat'])
m5 = df.merge(df5, how='left', on=['Long', 'Lat'])
m6 = df.merge(df6, how='left', on=['Long', 'Lat'])
m7 = df.merge(df7, how='left', on=['Long', 'Lat'])
m8 = df.merge(df8, how='left', on=['Long', 'Lat'])
m9 = df.merge(df9, how='left', on=['Long', 'Lat'])

### se vogliamo salvare i file intermedi
#m1.to_csv("19_2mtemperature.csv")
#m2.to_csv("19_mslpressure.csv")
#m3.to_csv("19_totalprecipitation.csv")
#m4.to_csv("19_postprocessgusts.csv")
#m5.to_csv("19_instantwindgusts.csv")
#m6.to_csv("19_u10.csv")
#m7.to_csv("19_v10.csv")

ma1 = m1.merge(m2, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma2 = ma1.merge(m3, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma3 = ma2.merge(m4, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma4 = ma3.merge(m5, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma5 = ma4.merge(m6, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma6 = ma5.merge(m7, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])

# calcola la velocità del vento  con Naegeli
ma6['wind speed 10'] = np.sqrt(ma6['u 10']* ma6['u 10'] + ma6['v 10'] * ma6['v 10'])
ma6['wind speed 100 Naeg'] = ma6['wind speed 10']*(0.233+0.656*np.log(104.75))

#print (ma6)
ma7 = ma6.merge(m8, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma8 = ma7.merge(m9, how='left', on=['Long', 'Lat', 'time', 'WTG Name', 'UP'])
ma8['wind speed 100'] = np.sqrt(ma8['u 100'] * ma8['u 100'] + ma8['v 100'] * ma8['v 100'])

print (ma8)

ma8.to_csv("allparamet.csv")

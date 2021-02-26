import os
import glob
import pandas as pd
import numpy as np
from datetime import timedelta

path = 'D:/Work Kate/OMNINEXT/Omni-energy/MATRIX/Dati_xy_Grib'

for folder in os.listdir(path):
    print(folder)
    day, month, year, hour = folder.split('_')

    for f in os.listdir(os.path.join(path, folder)):
        print(f)
        
        df1 = pd.read_csv(os.path.join(path, folder, f))
        df1 = df1[df1['time'] < 24.0]
        df1['date'] = year+'-'+month+'-'+day+' '+hour+':00:00'
        df1['date'] = df1['date'].astype('datetime64[ns]')
        df1['date'] += pd.to_timedelta(df1['time'], unit='hours')
        
print(df1.dtypes)        
print(df1.head())
print(df1.tail())


# definire il percorso dove si trovano le pale
df = pd.read_csv("D:/Work Kate/OMNINEXT/Omni-energy/MATRIX/5farm/farms.csv")

# # definire il percorso della working directory (dove si trovano tutti dati)
# os.chdir("D:/Work Kate/OMNINEXT/Omni-energy/MATRIX/Dati_xy_grib")

# ### carica e sistema i dati 
# ### Pressione
# df1 = pd.read_csv("19_01_2020_6000/Pressure.csv")
df1['pressure'] = df1['value']/100
df1 = df1.drop(columns=['fid', 'group', 'value'])
 
df1 = df1.rename(columns={"x": "Long", "y": "Lat"})
m1 = df.merge(df1, how='left', on=['Long', 'Lat'])

print(m1)

# print(m1)

#find out how to fix date time for each group member

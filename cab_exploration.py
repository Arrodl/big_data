import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from pandas import DataFrame
import time
import datetime
import math

def printTitle (title):
    print('{}\n____________________________________________'.format(title))

def determineDistanceBetweenCoordinates (from_latitude, from_longitude, to_latitude, to_longitude):
    rad_per_deg = math.pi / 80
    rkm = 6371
    rm = rkm * 1000
    dlat_rad = rad_per_deg * (from_latitude - to_latitude)
    dlon_rad = rad_per_deg * (from_longitude - to_longitude)
    from_lat_rad = from_latitude * rad_per_deg
    to_lat_rad = to_latitude * rad_per_deg
    square_sin_dlat_rand = (math.sin(dlat_rad) / 2) ^ 2
    square_sin_dlon_rand = (math.sin(dlon_rad) / 2) ^ 2
    cos_from_lat_rad = (math.cos(from_lat_rad))
    cos_to_lat_rad = (math.cos(to_lat_rad))
    a = square_sin_dlat_rand + cos_from_lat_rad * cos_to_lat_rad * square_sin_dlon_rand
    c = (2 * math.atan2(math.sqrt(abs(a)), math.sqrt(1 - abs(a))))
    return rm * c

# Load train data sample
df = pd.read_csv('./train.csv')

printTitle('Llaves')
print(df.columns)
# El axis es para saber que es una columna y no una fila
df = df.drop(['id'], axis = 1)
df = df.drop(['store_and_fwd_flag'], axis = 1)
df = df.drop(['vendor_id'], axis = 1)
df = df.drop(['passenger_count'], axis = 1)
df = df.drop(df[df.trip_duration > 141000].index)
constant = 57.29577951
df['pickup_latitude'] = df['pickup_latitude'].astype(float)
df['pickup_longitude'] = df['pickup_longitude'].astype(float)
df['dropoff_latitude'] = df['dropoff_latitude'].astype(float)
df['dropoff_longitude'] = df['dropoff_longitude'].astype(float)
df = df.assign(dif_long = (df['dropoff_longitude'] / constant) - df['pickup_longitude'] / constant)
df = df.assign(dif_lat = (df['dropoff_latitude'] / constant) - df['pickup_latitude'] / constant)
df = df.assign(a = (np.sin(df['dif_lat'] / 2)) * (np.sin(df['dif_lat'] / 2)) + (np.cos(df['pickup_latitude']) * np.cos(df['dropoff_latitude']) * (np.sin(df['dif_long'] / 2)) * (np.sin(df['dif_long'] / 2))))
df = df.assign(c = 2 * np.arcsin(np.sqrt(abs(df['a']))))
df = df.assign(distancia = (6371 * df['c']))
df['distancia'] = df['distancia'].astype(float)

# Formato a las fechas
df['pickup_datetime'] = df['pickup_datetime'].astype('datetime64[ns]')
df = df.assign(date = df['pickup_datetime'].dt.strftime("%d/%m/20%y"))
df = df.assign(hour = df['pickup_datetime'].dt.strftime("%H:%M:%S"))
df = df.assign(hour_two = df.hour.str[:2])
df = df.drop(['pickup_datetime'], axis = 1)
df = df.drop(['dropoff_datetime'], axis = 1)
df = df.drop(['hour'], axis = 1)
df['hour_two'] = df['hour_two'].astype(int)
df['date'] = df['date'].astype('datetime64[ns]')

df = df.assign(dia = df['date'].dt.strftime('%d'))
df = df.assign(mes = df['date'].dt.strftime('%m'))
df = df.assign(anio = df['date'].dt.strftime('20%y'))
df = df.assign(dia_semana = df['date'].dt.dayofweek)

df['dia'] = df['dia'].astype(int)
df['mes'] = df['mes'].astype(int)
df['anio'] = df['anio'].astype(int)

print(df.head())

df.hour_two.hist()
# sb.countplot(df['trip_duration'], label='Tiempo de viaje')
plt.show()

plt.scatter(df.distancia, df.hour_two)

plt.show()











# printTitle('Describe database')
# print(df.describe())
# df.trip_duration.plot()
# plt.show()
# df.trip_duration.hist()
# plt.show()


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
    c = (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    return rm * c

# Load train data sample
df = pd.read_csv('./train.csv')

printTitle('Llaves')
# El axis es para saber que es una columna y no una fila
df = df.drop(['id'], axis = 1)
df = df.drop(['store_and_fwd_flag'], axis = 1)
df = df.drop(['vendor_id'], axis = 1)
df = df.drop(['passenger_count'], axis = 1)
print(df.columns)

for row in df.iteritems():
    print(row)    

df.corr().plot()

plt.show()











# printTitle('Describe database')
# print(df.describe())
# df.trip_duration.plot()
# plt.show()
# df.trip_duration.hist()
# plt.show()


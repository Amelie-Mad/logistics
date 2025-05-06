import numpy as np
import pandas as pd
import utils

medellin = (6.251290,-75.5812)
bogota = (4.6100,-74.0833)

dist, time = utils.get_distance(bogota, medellin) 
print(f"Distance: {dist} km")
print(f"Time: {time} h")

data1 = pd.read_excel('Clientes Colombia Marzo 2.xlsx')
data2 = pd.read_excel('Clientes Colombia Marzo 3 (1).xlsx')

data = pd.concat([data1, data2], ignore_index=True)
data.to_csv('columbia_full.csv', index=False)

# Opening demand file
df = pd.read_csv('columbia_full.csv')
df.rename(columns={'FechaPlanInicioTransporte':'date', 'RegionalDistribucion': 'region','IDCentro':'Center_ID','CodigoCliente':'Client_ID'}, inplace=True)
df.drop(columns = ['Plan_Vol','plan_boxes','DocumentoTransporte','Ordered_vol'], inplace=True)

# Merging with the coordinates of the centers
coordinates_centers = pd.read_csv('Coordenadas CDs.csv', encoding='latin1')
coordinates_centers.drop(columns=['Nombre','Direccin','CD.1'], inplace=True)
coordinates_centers.rename(columns={'CD':'CD','Latitud':'Latitude_CD','Longitud':'Longitude_CD'}, inplace=True)

df = df.merge(coordinates_centers, how='inner', left_on='Center_ID', right_on='CD')

df.drop(columns=['CD'], inplace=True)
# Merging with the coordinates of the clients
coordinates_clients = pd.read_csv('Coordenadas Clientes.csv', encoding='latin1')
coordinates_clients = coordinates_clients[['CD CODE','CLIENT #','LATITUDE','LENGTH']]
coordinates_clients.rename(columns={'CD CODE':'Center_ID','CLIENT #':'Client_ID','LATITUDE':'Latitude_Client','LENGTH':'Longitude_Client'}, inplace=True)
coordinates_clients

df = df.merge(coordinates_clients, how='inner', left_on=['Client_ID','Center_ID'], right_on=['Client_ID','Center_ID'])

# Translating boxes into hL
df['ordered_volume'] = df['ordered_boxes'] * 0.0756

# Saving the final dataframe
df.to_csv('columbia_full_coordinates.csv', index=False)
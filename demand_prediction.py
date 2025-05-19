import numpy as np
import pandas as pd
import utils

medellin = (6.251290,-75.5812)
bogota = (4.6100,-74.0833)

dist, time = utils.get_distance(bogota, medellin) 
print(f"Distance: {dist} km")
print(f"Time: {time} h")

df = pd.read_csv('subproblem.csv')

# Get the distance between all customers and the depot, as well as between all customers

depot = (df['Latitude_CD'].iloc[0], df['Longitude_CD'].iloc[0])
print(depot)

clients = (df[['Latitude_Client', 'Longitude_Client']].values)
clients = np.unique(clients, axis=0)

dist_matrix, time_matrix = utils.distance_time_matrix(depot, clients, sample_size = len(clients))

print(dist_matrix)

dist_matrix.to_csv('distance_matrix_subproblem.csv', index=False)
time_matrix.to_csv('time_matrix_subproblem.csv', index=False)
#distance_matrix_full.to_csv('distance_matrix_subproblem.csv', index=False)
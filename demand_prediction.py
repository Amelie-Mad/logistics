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
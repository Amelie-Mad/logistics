import numpy as np
import pandas as pd
import utils

medellin = (6.251290,-75.5812)
bogota = (4.6100,-74.0833)

dist, time = utils.get_distance(bogota, medellin) 
print(f"Distance: {dist} km")
print(f"Time: {time} h")

df = pd.read_csv('subproblem.csv')



import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)  # show all columns
pd.set_option('display.width', 1000)   

data1 = pd.read_excel('Clientes Colombia Marzo 2.xlsx')
data2 = pd.read_excel('Clientes Colombia Marzo 3 (1).xlsx')

data = pd.concat([data1, data2], ignore_index=True)
data.to_csv('columbia_full.csv', index=False)

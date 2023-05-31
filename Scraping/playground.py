import pandas as pd

data_1 = pd.read_csv('data_products_id_1.csv')
data_2 = pd.read_csv('data_products_id_2.csv')

data = pd.concat([data_1, data_2])

data.to_csv('data_products_id.csv', index=False)

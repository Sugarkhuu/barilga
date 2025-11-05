import pandas as pd

df = pd.read_csv('data\data_uneguiplot_dailyprice.csv')

df['date'] = pd.to_datetime(df['date']) 
df.to_csv('data\data_uneguiplot_dailyprice.csv', index=False)
import pandas as pd

datadir = 'data/'
# Load the data 
df = pd.read_csv(datadir + 'data_uneguiplot.csv')

df.groupby('date')['price_m2'].agg(['median','mean', 'count']).to_csv(datadir + 'data_uneguiplot_dailyprice.csv')
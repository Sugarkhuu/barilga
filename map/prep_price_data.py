import pandas as pd

df_price = pd.read_csv('map/price_data.csv')
df_loc = pd.read_csv('map/location.csv')
df_geoloc = pd.read_csv('map/geo_location.csv')

df_geoloc.drop_duplicates(subset=['location_id','geo_location'], keep='first', inplace=True)

df_price = df_price.merge(df_loc, on='location')

df_price_stat = df_price.groupby('geo_location')['price_m2'].agg(['median', 'std', 'count']).reset_index()

df_price_stat = df_price_stat.merge(df_geoloc, left_on='geo_location', right_on='geo_location')

df_house_price =  df_price_stat[['location_id','median']]
df_house_price.columns = ['location_id','median_price']
df_house_price.to_csv('map/housing_prices.csv', index=False)
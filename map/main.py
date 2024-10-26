import pandas as pd
import geopandas as gpd
import plotly.express as px

# Load district boundaries from a GeoJSON file
geojson_path = 'map/ub.geojson'  # Replace with the path to your GeoJSON file
districts_geo = gpd.read_file(geojson_path)

# Load real estate price data
price_data_path = 'map/housing_prices.csv'  # Replace with the path to your CSV file
price_data = pd.read_csv(price_data_path)

# Merge GeoDataFrame with the price data on district ID
merged_data = districts_geo.merge(price_data, left_on='location_id', right_on='location_id')

# Convert GeoDataFrame to GeoJSON format for Plotly
geojson = merged_data.__geo_interface__

# Create the choropleth map with Plotly Express
fig = px.choropleth_mapbox(
    merged_data,
    geojson=geojson,
    locations='location_id',
    featureidkey='properties.location_id',
    color='median_price',
    color_continuous_scale="Viridis",
    range_color=(merged_data['median_price'].min(), merged_data['median_price'].max()),
    mapbox_style="open-street-map",  # Set to OpenStreetMap
    center={"lat": 47.9214, "lon": 106.9057},
    zoom=12,
    opacity=0.7,
    labels={'median_price': 'Median Price (₮)'},
    hover_name='mylocation',
    hover_data={'location_id': False, 'median_price': True}
)

# Update layout for better appearance
fig.update_layout(
    title="Ulaanbaatar Real Estate Prices by District",
    margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

html_file_path = 'map/ub_real_estate_prices.html'  # Replace with your desired file path
fig.write_html(html_file_path)

# Show the figure
fig.show()

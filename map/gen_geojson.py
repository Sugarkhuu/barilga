import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('map/geo_location.csv')

# Initialize the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Group by location_id and geo_location
grouped = df.groupby(['location_id', 'geo_location'])

# Iterate over each group
for (location_id, geo_location), group in grouped:
    # Prepare coordinates as a list of lists
    coordinates = group[['lon', 'lat']].values.tolist()

    # Create a feature for each location
    feature = {
        "type": "Feature",
        "properties": {
            "location_id": int(location_id),  # Convert to native int
            "geo_location": geo_location  # This can be in Cyrillic
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [coordinates]  # Wrap in an extra list for GeoJSON format
        }
    }

    # Append the feature to the features list
    geojson['features'].append(feature)

# Save the GeoJSON to a file with UTF-8 encoding
with open('map/ub.geojson', 'w', encoding='utf-8-sig') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

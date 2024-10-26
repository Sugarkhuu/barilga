import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('map/geo_location.csv')

# Initialize the GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Group by location_id and mylocation
grouped = df.groupby(['location_id', 'mylocation'])

# Iterate over each group
for (location_id, mylocation), group in grouped:
    # Prepare coordinates as a list of lists
    coordinates = group[['lon', 'lat']].values.tolist()

    # Create a feature for each location
    feature = {
        "type": "Feature",
        "properties": {
            "location_id": int(location_id),  # Convert to native int
            "mylocation": mylocation  # This can be in Cyrillic
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [coordinates]  # Wrap in an extra list for GeoJSON format
        }
    }

    # Append the feature to the features list
    geojson['features'].append(feature)

# Save the GeoJSON to a file with UTF-8 encoding
with open('output.geojson', 'w', encoding='utf-8-sig') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)

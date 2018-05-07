#Christina L. Marshall

import folium
import pandas as pd

collide = pd.read_csv("DUMBONoiseComplaints.csv")
mapCollisions = folium.Map(location=[40.7022621909, -73.9871760513])

for index,row in collide.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Complaint Type"]
    newMarker = folium.Marker(location=[lat,lon], popup=name)
    newMarker.add_to(mapCollisions)

mapCollisions.save(outfile= "myComplaints.html")

from datetime import datetime
import json
import requests
import csv
import folium
import itertools

url_api = requests.get ('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
url_json = url_api.json()
recorded_data = len(url_json['features'])
print(recorded_data)

for feature in url_json['features']:
    tm = datetime.fromtimestamp(0.001 * feature ['properties']['time'])
    time.append(tm.strftime('%Y-%m-%d %H:%M:%S'))
    magnitude.append(feature ['properties'] ['mag'])
    latitude.append(feature ['geometry'] ['coordinates'] [1])
    longitude.append(feature ['geometry'] ['coordinates'] [0])
    elevation.append(feature ['geometry'] ['coordinates'] [2])
    descr_loc.append(feature ['properties'] ['place'])

rows = zip (time, magnitude, latitude, longitude, elevation, descr_loc)

#create map object
m = folium.Map (location=[44.55, -103.46], zoom_start = 3)
tooltip = "Click For More Info"

#create markers
for tm, mag, lat, long, ele, des in rows:
    folium.Marker([lat, long], popup =f'<strong>{tm}, {des}, {mag}</strong>', tooltip = tooltip).add_to(m)
    m.save('map.html')

#packing all the lists into one
rows = zip (time, magnitude, latitude, longitude, elevation, descr_loc)

#write a csv file
with open('earthquake_data.csv', 'w') as f:
    wr = csv.writer(f)
    for row in rows:
        wr.writerow(row + '\n')
f.close()

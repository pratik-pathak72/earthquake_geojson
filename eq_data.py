from datetime import datetime
import json
import requests
import csv

# dt = datetime.fromtimestamp()
url_api = requests.get ('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson')
url_json = url_api.json()
# eq_time = list(url_json['features'][cnt])
recorded_data = len(url_json['features'])
print(recorded_data)
time = []
magnitude=[]
latitude=[]
longitude=[]
elevation=[]
descr_loc=[]

for feature in url_json['features']:
    tm = datetime.fromtimestamp(0.001 * feature ['properties']['time'])
    time.append(tm.strftime('%Y-%m-%d %H:%M:%S'))
    magnitude.append(feature ['properties'] ['mag'])
    latitude.append(feature ['geometry'] ['coordinates'] [1])
    longitude.append(feature ['geometry'] ['coordinates'] [0])
    elevation.append(feature ['geometry'] ['coordinates'] [2])
    descr_loc.append(feature ['properties'] ['place'])


rows = zip (time, magnitude, latitude, longitude, elevation, descr_loc)
with open('earthquake_data.csv', 'w',newline = '') as f:
    wr = csv.DictWriter(f, fieldnames = ['Time','Magnitude', 'Latitude', 'Longitude', 'Elevation', 'Place'])
    wr.writeheader()
    wr = csv.writer(f)
    for row in rows:
        wr.writerow(row)
f.close()

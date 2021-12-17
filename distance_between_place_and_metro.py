import requests
import pprint
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import geopy.distance
import time
'''def gettingWay(latitude1: float, longitude1: float, latitude2: float, longitude2: float):
    #ключи для маршрутизации
    #apikey = "86c1b598-967c-4d30-a1b5-44443c19521a"
    apikey ="b8bb5edd-6b7a-4cc3-9ddb-8670cc13eb14"
    #apikey = "pdct.1.1.20211130T095532Z.e8ffa8a131a613f3.a33d8ecdb70aa49e12118853fbe836b8821a0ecc"
    search_api_server = "https://api.routing.yandex.net/v2/route"
    search_params = {
        "apikey": apikey,
        "waypoints": f"{latitude1},{longitude1}|{latitude2},{longitude2}",
        "mode": "walking",
    }
    response = requests.get(search_api_server, params=search_params)
    result = response.json()
    pprint.pprint(result)
gettingWay(55.540416, 37.495097, 55.560074, 37.4414)
def deg2rad(deg: float):
    return (deg*np.pi)/180
def rad2deg(rad: float):
    return (rad * 180)/np.pi
def distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float):
    R = 6378.1
    latitude1r = deg2rad(latitude1)
    longitude1r = deg2rad(longitude1)
    latitude2r = deg2rad(latitude2)
    longitude2r = deg2rad(longitude2)
    u = np.sin((latitude2r-latitude1r)/2)
    v = np.sin((longitude2r - longitude1r) / 2)
    return 2.0 * R * np.arcsin(np.sqrt(u * u + np.cos(latitude1r) * np.cos(latitude2r) * v * v))'''

#print(distance(55.540416, 37.495097, 55.560074, 37.4414))
dff = pd.read_excel('adressesV1.xlsx')
d = []
for i in range(len(dff)):
    dist = geopy.distance.distance((dff.iloc[i, 2], dff.iloc[i, 3]), (dff.iloc[i, 5], dff.iloc[i, 6])).km
    d.append(dist)
    print(dist)
dff['Расстояние до метро'] = d
writer = pd.ExcelWriter('adressesV1.xlsx')
dff.to_excel(writer)
writer.save()
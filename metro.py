import requests
import pprint
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
def gettingMetroCoordinates(address: str, raion: str):
    #apikey = "18782173-7b98-4aaf-a8b4-75b3ec76d2de"
    apikey = "16459356-6cb8-4e79-94c1-c087e420e7f3"
    #apikey = "d3511d79-eb54-4ed0-b5d6-a357ca856414"
    #apikey = "4ef7b262-0374-48d3-97fb-5f463203bc29"
    #apikey = "8c2bca6a-0f79-4bd4-a694-4edb0229a24b"
    #apikey = "d6e7fef8-7fb3-4dea-897a-44f0edb61e1c"
    #apikey = "109eac31-0de9-4f02-b31f-029724ab6963"
    search_api_server = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "apikey": apikey,
        "text": f"метро, {raion}, {address}",
        "lang": "ru_RU",
        "type": "biz",
    }
    response = requests.get(search_api_server, params=search_params)
    result = response.json()
    pprint.pprint(result)

    if 'features' in result:
        for element in result['features']:
            if element['properties']['CompanyMetaData']['Categories'][0]['name'] == 'Станция метро':
                a, b = element['geometry']['coordinates']
                name = element['properties']['CompanyMetaData']['name']
                return a, b, name
                #print('a и b ', a, b)
                #print('name ', name)

dff = pd.read_excel('adressesV3.xlsx')
coordinates0 = []
coordinates1 = []
names = []
for i in range(len(dff)):
    res = gettingMetroCoordinates(dff.iloc[i, 1], dff.iloc[i, 4])
    print(i, dff.iloc[i, 0], dff.iloc[i, 3], res)
    if res is not None:
        #s = str(i) +  " " + str(coords[0]) + " " + str(coords[1]) + "\n"
        #f.write(s)

        coordinates1.append(res[1])
        coordinates0.append(res[0])
        names.append(res[2])
    else:
        coordinates1.append(0)
        coordinates0.append(0)
        names.append('-')
dff['Широта'] = coordinates1
dff['Долгота'] = coordinates0
dff['Название станции метро'] = names
print(dff)
writer = pd.ExcelWriter('adressesV5.xlsx')
dff.to_excel(writer)
writer.save()
import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium.plugins import FastMarkerCluster

def f_map():
    dff = pd.read_excel('adressesV1.xlsx')
    df = pd.read_excel('map.xlsx')
    raion = []
    proekt = []
    developer = []
    klass = []
    cena_za_kvm_min = []
    cena_za_kvm_sr = []
    cena_za_kvm_max = []
    for i in range(len(dff)):
        # df = pd.DataFrame(arr, columns=['lat', 'lon', 'link', 'string'])
        #string = f"{dff.at['Адрес', i]}.<br>"
        #r = dff.at[i, 'Адрес']
        c = pd.DataFrame(df.loc[df['Адрес корпуса'] == dff.at[i, 'Адрес']])
        #with pd.option_context('display.max_rows', None, 'display.max_columns',
                               #None):  # more options can be specified also
            #print(c)
        #indexes = [i for i in range(len(c))]
        #print(c)
        #c = c.reindex(range(len(c)), method='ffill')
        #print(c)
        #h.reindex(0, method='ffill')
        #print('--------------------------------')
        if len(c)!=0:
            x = str(c['Район'].mode())
            x = x.replace('0    ', '')
            x = x.replace('dtype: object', '')
            raion.append(x)

            x = str(c['Проект'].mode())
            x = x.replace('0    ', '')
            x = x.replace('dtype: object', '')
            proekt.append(x)

            x = str(c['Девелопер'].mode())
            x = x.replace('0    ', '')
            x = x.replace('dtype: object', '')
            developer.append(x)

            x = str(c['Класс'].mode())
            x = x.replace('0    ', '')
            x = x.replace('dtype: object', '')
            klass.append(x)

            cena_za_kvm_min.append(c['Цена за кв. метр'].min())
            cena_za_kvm_sr.append(c['Цена за кв. метр'].mean())
            cena_za_kvm_max.append(c['Цена за кв. метр'].max())
            #print(c['Район'][0])
        else:
            raion.append(0)
            proekt.append(0)
            developer.append(0)
            klass.append(0)
            cena_za_kvm_min.append(0)
            cena_za_kvm_sr.append(0)
            cena_za_kvm_max.append(0)
        print(i)

    #dff['string'] = s
    dff['Район'] = raion
    dff['Проект'] = proekt
    dff['Девелопер'] = developer
    dff['Класс'] = klass
    dff['Минимальная цена за кв.м']= cena_za_kvm_min
    dff['Средняя цена за кв.м'] = cena_za_kvm_sr
    dff['Максимальная цена за кв.м'] = cena_za_kvm_max
    dff.to_excel("adressesV3.xlsx")

f_map()
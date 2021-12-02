import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium.plugins import FastMarkerCluster


def interactive_map():
    st.title("Карта")  # change
    # дальше будут идти сэты со списками девелоперов, классов и тд
    callback = ("function (row) {"
                "var icon = L.icon({iconUrl: row[2], iconSize: [24, 24], iconAnchor: [16, 37], popupAnchor: [0, -28]});"
                "var marker = L.marker([row[0], row[1]], {icon: icon}); "
                "var popup = L.popup({maxWidth: '400'});"
                "const display_text = {text: row[3]};"
                "var mytext = $(`<div id='mytext' class='display_text' "
                "style='width: 100.0%; height: 100.0%;'> ${display_text.text}</div>`)[0];"
                "popup.setContent(mytext);"
                "marker.bindPopup(popup);"
                "return marker};")
    dff = pd.read_excel('adresses.xlsx')
    location = [55.7522, 37.61200]
    zoom_start = 10
    # 55.7522, 37.6156
    s = []
    for i in range(len(dff)):
        # df = pd.DataFrame(arr, columns=['lat', 'lon', 'link', 'string'])
        # string = f"{dff.at['Адрес', i]}.<br>"
        str = dff.at[i, 'Адрес']
        s.append(str)
    dff['string'] = s
    m = folium.Map(location=location, zoom_start=zoom_start)
    m.add_child(
        FastMarkerCluster(dff[['Широта', 'Долгота', 'string']].values.tolist(), callback=callback))
    with st.container():
        folium_static(m, width=1350)


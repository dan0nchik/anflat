import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
from folium.plugins import FastMarkerCluster


def interactive_map():
    st.title("Карта")  # change
    # дальше будут идти сэты со списками девелоперов, классов и тд
    callback = ("function (row) {"
                "var icon = L.AwesomeMarkers.icon({ icon: 'icon',markerColor: 'red'});"
                "var marker = L.marker([row[0], row[1]], {icon: icon}); "
                "var popup = L.popup({maxWidth: '300'});"
                "const display_text = {text: row[2]};"
                "var mytext = $(`<div id='mytext' class='display_text' "
                "style='width: 100.0%; height: 100.0%;'> ${display_text.text}</div>`)[0];"
                "popup.setContent(mytext);"
                "marker.bindPopup(popup);"
                "return marker};")

    dff = pd.read_excel('adressesV1.xlsx')
    # print(dff)
    location = [55.7522, 37.61200]
    zoom_start = 10
    # 55.7522, 37.6156
    s = []
    for i in range(len(dff)):
        # df = pd.DataFrame(arr, columns=['lat', 'lon', 'link', 'string'])
        r = f"<br><b>Адрес:</b> {dff.iloc[i, 1]}.<br>"
        r = r + f"<br><b>Район:</b> {dff.iloc[i, 8]}<br>"
        r = r + f"<br><b>Проект:</b> {dff.iloc[i, 9]}<br>"
        r = r + f"<br><b>Девелопер:</b> {dff.iloc[i, 10]}<br>"
        r = r + f"<br><b>Класс:</b> {dff.iloc[i, 11]}<br>"
        r = r + f"<br><b>Минимальная цена за кв.м:</b> {dff.iloc[i, 12]}<br>"
        r = r + f"<br><b>Средняя цена за кв.м:</b> {dff.iloc[i, 13]}<br>"
        r = r + f"<br><b>Максимальная цена за кв.м:</b> {dff.iloc[i, 14]}<br>"
        r = r + f"<br><b>Ближайшая станция метро :</b> {dff.iloc[i, 4]} в <b>{round(float(dff.iloc[i, 7]), 1)} км</b><br>"
        s.append(r)

    dff['текст'] = s
    m = folium.Map(location=location, zoom_start=zoom_start)
    m.add_child(
        FastMarkerCluster(dff[['Широта', 'Долгота', 'текст']].values.tolist(), callback=callback))
    container = st.container()
    with container:
        folium_static(m, width=1350)

# st.set_page_config(layout="wide")
# pages = {'Интерактивная карта': interactive_map}
# st.sidebar.title('Меню')
# choice = st.sidebar.radio("Выберите страницу:", tuple(pages.keys()))
# pages[choice]()

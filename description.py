import streamlit as st


def description_page():
    st.write('# Описание датасета')
    st.write('Здесь вы можете увидеть различную статистику по исходному датасету')
    st.write('### Топ девелоперов')
    st.image('charts/Bar charts/developer.jpg', use_column_width=True)
    st.write('### Районы')
    st.image('charts/Bar charts/Район.jpg', use_column_width=True)
    st.write('### Класс')
    st.image('charts/Bar charts/Класс.jpg', use_column_width=True)
    st.write('### Тип сделки')
    st.image('charts/Bar charts/Тип сделки.jpg', use_column_width=True)
    st.write('### Распределение площади')
    st.image('charts/Histograms/Площадь.jpg', use_column_width=True)
    st.write('### Распределение цены')
    st.image('charts/Histograms/Цена за кв. метр.jpg', use_column_width=True)
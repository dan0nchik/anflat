import streamlit as st
from map_page import interactive_map
from graphs import graph_page
from predict import prediction_page

st.set_page_config(layout="wide")
pages = {'Интерактивная карта': interactive_map, 'Факторы, влияющие на цену': graph_page,
         'Предсказание цены': prediction_page}
st.sidebar.title('Меню')
choice = st.sidebar.radio("Выберите страницу:", tuple(pages.keys()))
pages[choice]()

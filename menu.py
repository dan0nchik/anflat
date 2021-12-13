import streamlit as st
from map_page import interactive_map
from graphs import graph_page
from predict import prediction_page
import os

if not os.path.isdir('Streamlit-Image-Carousel/frontend/public'):
    print('INSTALLING NPM MODULES')
    os.system('cd Streamlit-Image-Carousel/frontend/')
    os.system('cd Streamlit-Image-Carousel/frontend/; npm i; npm run build; cd ../../')

st.set_page_config(layout="wide")
pages = {'Интерактивная карта': interactive_map, 'Факторы, влияющие на цену': graph_page,
         'Предсказание цены': prediction_page}
st.sidebar.title('Меню')
choice = st.sidebar.radio("Выберите страницу:", tuple(pages.keys()))
pages[choice]()

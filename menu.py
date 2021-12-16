import streamlit as st
from map_page import interactive_map
from graphs import graph_page, carousel
from predict import prediction_page
from preprocess import page
import os

st.set_page_config(layout="wide")
# trying to install npm in streamlit mmmmmmm
# if not os.path.isdir('Streamlit-Image-Carousel/frontend/public'):
#     print('INSTALLING NPM MODULES')
#     os.system('cd Streamlit-Image-Carousel/frontend/')
#     os.system('cd Streamlit-Image-Carousel/frontend/; npm i; npm run build; cd ../../')

pages = {'Предобработка данных': page, 'Карта квартир': interactive_map,
         # 'Факторы, влияющие на цену': carousel,
         'Предсказание цены': prediction_page}
st.sidebar.title('Меню')
choice = st.sidebar.radio("Выберите страницу:", tuple(pages.keys()))
pages[choice]()

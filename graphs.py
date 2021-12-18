import os
import streamlit as st


def carousel():
    # imageCarouselComponent = components.declare_component("image-carousel-component",
    #                                                       path="Streamlit-Image-Carousel/frontend/public")
    # st.markdown('# Зависимость цены от различных факторов')
    # st.write('В данном разделе представлены графики зависимости цены на квартиры в Новой Москве от различных '
    #          'параметров')
    # # st.image('charts/Графики для Девелопера.png')
    # # st.image('charts/Графики для Срок ввода в эксплуатацию - Договор.png')
    # # st.image('charts/Графики для Срок ввода в эксплуатацию - Старт продаж.png')
    # graph_urls = {
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/contract_date.png?token'
    #     '=ALBMFIBBYO2KGCB4P7G2IBDBXG2TA': 'contract_date',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/dev.png?token=ALBMFIHBJSPUTILOVRT3BRTBXG2YO': 'dev',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_contract.png?token'
    #     '=ALBMFIHHEG4GPYHVYKBVKNTBXG2ZC': 'exp_contract',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_from_contract.png?token'
    #     '=ALBMFIC227CQLCEE4BO5ESDBXG2ZS': 'exp_from_contract',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_sales.png?token'
    #     '=ALBMFIHBPPEGPLVKCQ74NILBXG22C': 'exp_sales',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/finishing.png?token'
    #     '=ALBMFIEAVZ7TKYOIROQ6NTTBXG22S': 'finishing',
    #     'https://github.com/dan0nchik/anflat/blob/master/buttons/price_exp.png?raw=true': 'price_exp',
    #     'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/square.png?raw=true': 'square'
    # }
    # selectedImageUrl = imageCarouselComponent(imageUrls=list(graph_urls.keys()), height=100)
    # avg_price = os.listdir('charts/average price')
    # delta_price = os.listdir('charts/price delta')
    # if selectedImageUrl is not None:
    #     st.image('charts/average price/' +  str(list(filter(lambda x: graph_urls[selectedImageUrl] in x, avg_price))[0]))
    #     st.image('charts/price delta/' + str(list(filter(lambda x: graph_urls[selectedImageUrl] in x, delta_price))[0]))
    pass


def graph_page():
    st.markdown('# Анализ')
    st.write('В данном разделе представлены графики, представляющие различные типы зависимости цены за кв. метр от '
             'различных '
             'факторов')
    st.latex(r'\textbf{Формула зависимости: } y = 82.702x + 124396')
    st.image('charts/срок в экспозиции до момента сделки ЭКОНОМ.png',use_column_width=True)
    st.latex(r'\textbf{Формула зависимости: } y = -2E-05x^2 + 0.2147x + 119218')
    st.image('charts/Срок_в_экспозиции_до_момента_сделки (КОМФОРТ).png',use_column_width=True)
    st.latex(r'\textbf{Формула зависимости: } y = 3.3803x + 132636')
    st.image('charts/срок ввода в экспл - старт продаж ЭКОНОМ.png',use_column_width=True)
    st.latex(r'\textbf{Формула зависимости: } y = 0.0001x^3 - 0.4827x^2 + 489.24x')
    st.image('charts/срок ввода в эксплуатацию - старт продаж КОМФОРТ.png',use_column_width=True)
    st.latex(r'\textbf{Площадь в бизнес классе}')
    st.image('charts/Зависимость цены от Площадь согласно ПД для квартир Бизнес классаpng.png',use_column_width=True)
    st.latex(r'\textbf{Площадь в комфорт классе}')
    st.image('charts/Зависимость цены от Площадь согласно ПД для квартир Комфорт классаpng.png',use_column_width=True)
    st.write('### 👆 Вывод: В разных классах цена меняется по-разному')

    st.image('charts/расстояние до метро.png',use_column_width=True)
    st.write('### 👆 Вывод: близость к метро действительно влияет на стоимость')
    st.image('charts/девелоперы по классам.png',use_column_width=True)
    st.write('### 👆 Вывод: больше девелоперов строят для класса комфорт')
    st.image('charts/dev_biz.jpg', use_column_width=True)
    st.image('charts/dev_eco.jpg', use_column_width=True)
    st.image('charts/dev_komf.jpg', use_column_width=True)
    st.write('### 👆 Вывод: наибольший разброс цен наблюдается в комфорт классе')



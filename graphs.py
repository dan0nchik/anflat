import os
import streamlit as st


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



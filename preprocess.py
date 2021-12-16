import streamlit as st
import pandas as pd
import os


@st.cache
def read_data(path):
    data = pd.read_csv(path, index_col=0)
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    return data


def page():
    st.markdown('# Предобработка данных')
    st.write('### Было:')
    st.markdown('Длина: **64678**')
    st.markdown('Кол-во колонок: **42**')
    st.dataframe(read_data('data.csv').head(3))
    st.write('### Стало:')
    st.markdown('Длина: **59346**')
    st.markdown('Кол-во колонок: **28**')
    st.dataframe(read_data('ml.csv').head(3))
    st.write("## Как это было сделано?")
    st.write("##### Удалены колонки:")
    with st.expander('Какие?'):
        st.write(
            f"{['ID проекта', 'ID корпуса', 'Локация', 'ID лота', 'Расчетный бюджет объекта', 'Кол-во месяцев обременения', 'Рост бюджета покупки за период экспонирования', 'Округ', 'Месяц и год даты договора', 'Месяц и год даты регистрации', 'Проект']}")
    st.write("##### Заполнены/удалены пропуски:")
    st.write(
        {"Секция": '4356 пустых заполнены средними', 'Цена за кв, метр': "907 удалены", 'Кол-во комнат': "445 удалены"})
    st.write("##### Конвертированы даты:")
    st.image(os.path.join(os.getcwd(), 'data_preparation_img', 'dates.jpg'), width=650, use_column_width=True)
    st.write("##### Извлечены числа из длинных строк:")
    st.image(os.path.join(os.getcwd(), 'data_preparation_img', 'discounts.jpg'), width=350, use_column_width=True)
    st.write("##### Добавлено расстояние до метро:")
    with st.container():
        st.image(os.path.join(os.getcwd(), 'data_preparation_img', 'metro.jpg'), width=440, use_column_width=True)
        st.write('С помощью API Яндекс Карт создана колонка "Расстояние до метро" на основе геокоординат 366 адресов '
                 'корпусов')
    st.write("##### Созданы колонки на основе разницы дат")
    st.image(os.path.join(os.getcwd(), 'data_preparation_img', 'date_diff.jpg'), width=440, use_column_width=True)
    st.write('Срок ввода в эксплуатацию - Старт продаж;', 'Срок ввода в эксплуатацию - Договор;',
             'Срок в экспозиции до момента сделки')
    st.write("##### Категориальные колонки закодированы")
    st.write('Пример:')
    st.write({'Бизнес': 0,
              'Комфорт': 1,
              'Эконом': 2})
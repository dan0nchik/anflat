import streamlit as st
import streamlit.components.v1 as components
import os

def graph_page():
    imageCarouselComponent = components.declare_component("image-carousel-component",
                                                          path="Streamlit-Image-Carousel/frontend/public")
    st.markdown('# Зависимость цены от различных факторов')
    st.write('В данном разделе представлены графики зависимости цены на квартиры в Новой Москве от различных '
             'параметров')
    # st.image('charts/Графики для Девелопера.png')
    # st.image('charts/Графики для Срок ввода в эксплуатацию - Договор.png')
    # st.image('charts/Графики для Срок ввода в эксплуатацию - Старт продаж.png')
    graph_urls = {
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/contract_date.png?token'
        '=ALBMFIBBYO2KGCB4P7G2IBDBXG2TA': 'contract_date',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/dev.png?token=ALBMFIHBJSPUTILOVRT3BRTBXG2YO': 'dev',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_contract.png?token'
        '=ALBMFIHHEG4GPYHVYKBVKNTBXG2ZC': 'exp_contract',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_from_contract.png?token'
        '=ALBMFIC227CQLCEE4BO5ESDBXG2ZS': 'exp_from_contract',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/exp_sales.png?token'
        '=ALBMFIHBPPEGPLVKCQ74NILBXG22C': 'exp_sales',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/finishing.png?token'
        '=ALBMFIEAVZ7TKYOIROQ6NTTBXG22S': 'finishing',
        'https://github.com/dan0nchik/anflat/blob/master/buttons/price_exp.png?raw=true': 'price_exp',
        'https://raw.githubusercontent.com/dan0nchik/anflat/master/buttons/square.png?raw=true': 'square'
    }
    selectedImageUrl = imageCarouselComponent(imageUrls=list(graph_urls.keys()), height=100)
    avg_price = os.listdir('charts/average price')
    if selectedImageUrl is not None:
        st.image('charts/average price/'+str(list(filter(lambda x: graph_urls[selectedImageUrl] in x, avg_price))[0]))

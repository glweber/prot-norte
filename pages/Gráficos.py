import streamlit as st
import pandas as pd
import plotly.express as px
import os


df = pd.read_csv('src/ITAI.csv')

st.set_page_config(page_title='NORTE - Gráficos :)', page_icon='src/img/sat.png', layout='wide')

st.title('Gráficos - ITAI')

# st.title('Bem-vindo a demonstração da biblioteca Streamlit para a criação de paineis de dados interativos!', ali)
st.markdown("<h1 style='text-align: left; color: white;'>Bem-vindo a demonstração da biblioteca Streamlit <br/> para a criação de paineis de dados interativos!</h1>",
            unsafe_allow_html=True)

st.divider()

st.markdown("<h2 style='text-align: left; color: white;'>Possibilidades da Biblioteca</h2>",
            unsafe_allow_html=True)

col1, col2 = st.columns(2, gap='medium')

with col1:
    equation = st.text_area(
        'Podemos criar áreas de texto para compilar fórmulas, entrada de texto e muitos afins.'
        'Caso queira testar, basta alterar o texto abaixo e pressionar Cntrl + Enter na caixa de texto que o texto será compilado!',
        'e^{i\pi} + 1 = 0'
    )


with col2:
    st.latex(equation)

st.divider()

st.subheader('Caso queira colocar alguma métrica e afins. É possível coletar respostas de API (previsão do tempo, bolsa de valores e afins)')

st.text('Aqui n tem nada de requisição, mas fica a demonstração visual :)')

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
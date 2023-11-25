import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

df = pd.read_csv('src/ITAI.csv')

df['data'] = pd.to_datetime(df['data'])

st.set_page_config(page_title='NORTE - Gráficos :)', page_icon='src/img/sat.png', layout='wide')

st.title('Gráficos - ITAI')

st.divider()

# If x Data
if_data = px.line(df, x='data', y='If', color='satelite', title='If x Data | Satélite', template='plotly')
st.plotly_chart(if_data, use_container_width=True, height= 600)


st.header('Mapa: gIfv x satélite')


map_gIfv = px.scatter_mapbox(df, lat="IPPlat", lon="IPPlon", color="satelite", size="gIfv",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=22, zoom=5,
                  mapbox_style="carto-positron")

map_gIfv.update_layout(height=800)

st.plotly_chart(map_gIfv, use_container_width=True, height=800)

st.divider()


st.header('Mapa: gIfv x satélite | animado')
st.subheader('Ano de 2017 | só esperar um tiquin q ele carrega :)')

df_filtered = df[(df['data'] >= '2017-01-01') & (df['data'] <= '2017-12-31')]

map_gIfv = px.scatter_mapbox(df_filtered, lat="IPPlat", lon="IPPlon", color="satelite", size="gIfv",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=33, zoom=5,
                  mapbox_style="carto-positron", animation_frame='data')

map_gIfv.update_layout(height=800)

st.plotly_chart(map_gIfv, use_container_width=True, height=800)





















import os, sys
path_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(path_file)

import streamlit as st
from streamlit_folium import folium_static

from packages import etl
from packages import layouts
from packages import utils

import importlib
importlib.reload(utils)
importlib.reload(layouts.home)

df = etl.extract.csv(path_file+'/data/processed/zomato.csv')

st.set_page_config(
    page_title='Home',
    layout="wide"
)

# ======================================================================================================
# SideBar
# ======================================================================================================

st.sidebar.title('Fome Zero')

st.sidebar.markdown('## Filtros')

# Filtro de países
country_options = st.sidebar.multiselect(
    label='Escolha os países que deseja visualizar as informações:',
    options=utils.get_countries(df),
    default=utils.DEFAUT_COUNTRIES
)

df_filtered = df[df['country_name'].isin(country_options)].reset_index()

# ======================================================================================================
# Content
# ======================================================================================================

st.title('Fome Zero!')
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')
st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        col1.metric('Restaurantes Cadastrados', df.restaurant_id.nunique())
    with col2:
        col2.metric('Países Cadastrados', df.country_name.nunique())
    with col3:
        col3.metric('Cidades Cadastrados', df.city.nunique())
    with col4:
        col4.metric('Avaliações Feitas na Plataforma',  f"{df.votes.sum():,}".replace(",", "."))
    with col5:
        col5.metric('Tipos de Culinárias Oferecidas', df.cuisines.nunique())
with st.container():
    map = layouts.home.maps(df_filtered)
    folium_static(
        map, 
        width=1024, 
        height=600)

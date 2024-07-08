import os, sys
path_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(path_file)

import streamlit as st
from streamlit_folium import folium_static

from packages import etl
from packages import layouts
from packages import utils

import importlib
importlib.reload(utils)
importlib.reload(layouts.countries)

st.set_page_config(
    page_title="Countries", 
    page_icon="🌍", 
    layout="wide")

df = etl.extract.csv(path_file+'/data/processed/zomato.csv')

# ======================================================================================================
# SideBar
# ======================================================================================================

st.sidebar.markdown('### Filtros')

# Filtro de países
country_options = st.sidebar.multiselect(
    label='Escolha os países que deseja visualizar as informações:',
    options=utils.get_countries(df),
    default=utils.DEFAUT_COUNTRIES
)

# df_filtered = utils.get_filtered_data(data=df, countries=country_options)
df_filtered = df[df['country_name'].isin(country_options)]

# ======================================================================================================
# Content
# ======================================================================================================

st.markdown('# 🌍 Visão Países')

with st.container():
    st.plotly_chart(
        layouts.countries.plot_restaurants_by_country(df_filtered), 
        use_container_width=True)
    
with st.container():
    st.plotly_chart(
        layouts.countries.plot_cities_by_country(df_filtered),
        use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            layouts.countries.plot_rating_by_country(df_filtered), 
            use_container_width=True)
        
    with col2:
        st.plotly_chart(
            layouts.countries.plot_cost_for_two_by_country(df_filtered), 
            use_container_width=True)
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from packages import etl
from packages import layouts
from packages import utils

import streamlit as st
import importlib
importlib.reload(utils)
importlib.reload(layouts.cuisines)

# ======================================================================================================
# Config and Load Data
# ======================================================================================================

st.set_page_config(
    page_title="Cuisines", 
    page_icon="🍽️", 
    layout="wide")

df = etl.extract.csv('data/processed/zomato.csv')

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

total_restaurants = st.sidebar.slider(
    'Selecione a quantidade de restaurantes que deseja visualizar:',
    value=10,
    min_value=1,
    max_value=20
)

# Filtro de cozinhas
cuisines_options = st.sidebar.multiselect(
    label='Escolha os tipos de culinária:',
    options=utils.get_cuisines(df),
    default=utils.DEFAUT_CUISINES
)

df_filtered = df[df['country_name'].isin(country_options)]
df_top5 = layouts.cuisines.top5_best_restaurants_cuisines(df_filtered)

# ======================================================================================================
# Content
# ======================================================================================================

st.markdown('# 🍽️ Visão Tipos de Cozinhas')

if df_filtered.empty == False:
    with st.container():
        st.markdown('## Melhores Restaurantes dos Principais tipos Culinários')
        col1, col2, col3, col4, col5 = st.columns(5)
        for col, item in zip([col1, col2, col3, col4, col5], df_top5.values):
            country, cuisine, rating, restaurant = item
            if restaurant != None:
                with col:
                    cuisine_colored = f'<span style="color:orange">{cuisine}</span>'
                    st.markdown(f'### **{cuisine_colored}**', unsafe_allow_html=True)
                    st.metric(label=f'{restaurant}', value=f'{rating}/5.0')
                    st.markdown(f'##### {country}', unsafe_allow_html=True)

    with st.container():
        st.title('Top 10 Restaurantes')
        st.dataframe(layouts.cuisines.top_restaurants(df_filtered, total_restaurants))

    with st.container():
        col1, col2 = st.columns(2)
        for col, ascending in zip([col1, col2], [False, True]):
            with col:
                st.plotly_chart(layouts.cuisines.plot_top_cuisines(df, total_restaurants, ascending=ascending))

    # ======================================================================================================
    # Content
    # ======================================================================================================

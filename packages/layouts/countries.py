import plotly.express as px

# ======================================================================================================
# Plot
# ======================================================================================================

def plot_restaurants_by_country(df):
    grouped = (df[["restaurant_id", "country_name"]]
               .groupby(['country_name'])
               .count()
               .reset_index()
               .sort_values(['restaurant_id'], ascending=False)
               .head(6))
    fig = px.bar(grouped, 
                 x='country_name', 
                 y='restaurant_id', 
                 labels={
                     'country_name': 'Países', 
                     'restaurant_id': 'Quantidade de Restaurantes'},
                 title='Quantidade de Restaurantes Registrados por País',
                 text_auto=True)
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'
    })
    return fig

def plot_cities_by_country(df):
    grouped = (df[["city", "country_name"]]
               .groupby(['country_name'])
               .nunique()
               .reset_index()
               .sort_values(['city'], ascending=False)
               .head(6))
    fig = px.bar(grouped, 
                 x='country_name', 
                 y='city', 
                 labels={
                     'country_name': 'Países', 
                     'city': 'Quantidade de Cidades'},
                 title='Quantidade de Cidades Registradas por País',
                 text_auto=True)
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'
    })
    return fig

def plot_rating_by_country(df):
    grouped = (df[["votes", "country_name"]]
               .groupby(['country_name'])
               .mean()
               .reset_index()
               .sort_values(['votes'], ascending=False)
               .head(6))
    fig = px.bar(grouped, 
                 x='country_name', 
                 y='votes', 
                 labels={
                     'country_name': 'Países', 
                     'votes': 'Quantidade de Avaliações'},
                 title='Média de Avaliações feitas por País',
                 text_auto=True)
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'
    })
    fig.update_traces(texttemplate='%{y:.2f}')
    return fig

def plot_cost_for_two_by_country(df):
    grouped = (df[["average_cost_for_two", "country_name"]]
               .groupby(['country_name'])
               .mean()
               .reset_index()
               .sort_values(['average_cost_for_two'], ascending=False)
               .head(6))
    fig = px.bar(grouped, 
                 x='country_name', 
                 y='average_cost_for_two', 
                 labels={
                     'country_name': 'Países', 
                     'average_cost_for_two': 'Preço do Prato para duas Pessoas'},
                 title='Média de Preço de um Prato para duas Pessoas por País',
                 text_auto=True)
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'
    })
    fig.update_traces(texttemplate='%{y:.2f}')
    return fig


import plotly.express as px

# ======================================================================================================
# Plot
# ======================================================================================================

def plot_top_cities_most_restaurants(df):
    grouped = (df[["restaurant_id", "city", "country_name"]]
               .groupby(['country_name', 'city'])
               .count()
               .sort_values(["restaurant_id", "city"], ascending=[False, True])
               .reset_index()
               .head(10))
    
    fig = px.bar(grouped, 
                 x='city', 
                 y='restaurant_id', 
                 text_auto=True,
                 color="country_name",
                 title='Top 10 Cidades com mais Restaurantes na Base de Dados',
                 labels={
                     'city': 'Cidade', 
                     'restaurant_id': 'Quantidade de Restaurantes',
                     'country_name': 'País'},
                 )
    
    # Centralizar o título
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'})
    
    # Formatar os valores com 2 dígitos após a vírgula
    fig.update_traces(texttemplate='%{y:.2f}')
    
    return fig

def plot_top_cities_highest_ratings(df):
    grouped = (df.loc[
            (df["aggregate_rating"] > 4), 
            ["aggregate_rating", "city", "country_name"]]
        .groupby(['country_name', 'city'])
        .count()
        .sort_values(["aggregate_rating", "city"], ascending=[False, True])
        .reset_index()
        .head(7))
    
    fig = px.bar(grouped, 
                 x='city', 
                 y='aggregate_rating', 
                 text_auto=True,
                 color="country_name",
                 title='Top 7 Cidades com mais Restaurantes com Média de Avaliação acima de 4',
                 labels={
                     'city': 'Cidade', 
                     'aggregate_rating': 'Quantidade de Restaurantes',
                     'country_name': 'País'},
                 )
    
    # Centralizar o título
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'})
    
    # Formatar os valores com 2 dígitos após a vírgula
    fig.update_traces(texttemplate='%{y:.2f}')
    
    return fig

def plot_top_cities_lowest_ratings(df):
    grouped = (df.loc[
            (df["aggregate_rating"] < 2.5), 
            ["aggregate_rating", "city", "country_name"]]
        .groupby(['country_name', 'city'])
        .count()
        .sort_values(["aggregate_rating", "city"], ascending=[False, True])
        .reset_index()
        .head(7))
    
    fig = px.bar(grouped, 
                 x='city', 
                 y='aggregate_rating', 
                 text_auto=True,
                 color="country_name",
                 title='Top 7 Cidades com mais Restaurantes com Média de Avaliação acima de 4',
                 labels={
                     'city': 'Cidade', 
                     'aggregate_rating': 'Quantidade de Restaurantes',
                     'country_name': 'País'},
                 )
    
    # Centralizar o título
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'})
    
    # Formatar os valores com 2 dígitos após a vírgula
    fig.update_traces(texttemplate='%{y:.2f}')
    
    return fig


def plot_top_cities_by_cuisine_variety(df):
    grouped = (df[["cuisines", "city", "country_name"]]
        .groupby(['country_name', 'city'])
        .nunique()
        .sort_values(["cuisines", "city"], ascending=[False, True])
        .reset_index()
        .head(10))
    
    fig = px.bar(grouped, 
                 x='city', 
                 y='cuisines', 
                 text_auto=True,
                 color="country_name",
                 title='Top 10 Cidades mais restaurantes com tipos culinários distintos',
                 labels={
                     'city': 'Cidade', 
                     'cuisines': 'Quantidade de Tipos de Culinária Única',
                     'country_name': 'País'},
                 )
    
    # Centralizar o título
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'})
    
    # Formatar os valores com 2 dígitos após a vírgula
    fig.update_traces(texttemplate='%{y:.2f}')
    
    return fig
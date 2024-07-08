import pandas as pd
import plotly.express as px

# ======================================================================================================
# Dataframe
# ======================================================================================================

def matrics(data, cuisine, ascending=False, total_lines=1):
    df_filtered = data[data['cuisines'] == cuisine].copy()
    df_filtered['index'] = df_filtered.index
    df_result = (df_filtered[['index', 'cuisines', 'restaurant_name', 'aggregate_rating', 'country_name']]
                    .sort_values(['aggregate_rating', 'index'], ascending=[ascending, True])
                    .head(total_lines))
    df_result = df_result.drop('index', axis=1)
    if not df_result.empty:
        return (
            df_result.cuisines.iloc[0],
            df_result.country_name.iloc[0],
            df_result.restaurant_name.iloc[0],
            df_result.aggregate_rating.iloc[0]
        )
    else:
        return None, None, None, None
    
def top_restaurants(df, total_restaurants=10):
    columns = [
        'restaurant_id',
        'restaurant_name',
        'country_name',
        'city',
        'cuisines',
        'average_cost_for_two',
        'aggregate_rating',
        'votes'
    ]
    return (df[columns]
            .sort_values(['aggregate_rating'], ascending=False)
            .head(total_restaurants))

def top5_restaurants_cuisines(df, ascending=False):
    cols = [
        'country_name', 
        'cuisines', 
        'aggregate_rating', 
        'restaurant_name'
    ]
    cuisines = df.cuisines.unique()
    result = (
        df[df['cuisines']
           .isin(cuisines)]
           .sort_values(by='aggregate_rating', ascending=ascending)
           .drop_duplicates(subset='cuisines', keep='first')
           .head(5)
    )
    return result[cols]

# ======================================================================================================
# Plot
# ======================================================================================================

def plot_top_cuisines(df, total_restaurants, ascending=True):
    
    cuisines = df.cuisines.unique()
    countries = df.country_name.unique()

    label = 'Piores' if ascending else 'Melhores'
    grouped = (df.loc[
        (df["country_name"].isin(countries)) &
        (df["cuisines"].isin(cuisines)), 
        ["aggregate_rating", "cuisines"]]
        .groupby(['cuisines'])
        .mean()
        .sort_values(["aggregate_rating"], ascending=ascending)
        .reset_index()
        .head(total_restaurants))
    
    fig = px.bar(grouped, 
                 x='cuisines', 
                 y='aggregate_rating', 
                 text_auto=True,
                 title=f'Top 10 {label} TIpo de Culinárias',
                 labels={
                     'aggregate_rating': 'Média da Avaliação Média',
                     'cuisines': 'Tipo de Culinária'},
                 )
    
    # Centralizar o título
    fig.update_layout(title={
        'x': 0.5, 
        'xanchor': 'center'})
    
    # Formatar os valores com 2 dígitos após a vírgula
    fig.update_traces(texttemplate='%{y:.2f}')
    
    return fig

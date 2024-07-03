import plotly.express as px
import folium
from folium.plugins import MarkerCluster

# ======================================================================================================
# Plot
# ======================================================================================================

def maps(df, initial_zoom=2.4):    
    # Verifique se há dados suficientes para definir a localização inicial do mapa
    if df.empty:
        return folium.Map(
            location=[0, 0], 
            zoom_start=2)
    
    latitude = df['latitude'][0]
    longitude = df.loc[0, 'longitude']
    
    # Inicialize o mapa com a localização inicial e o zoom inicial
    map = folium.Map(
        location=[latitude, longitude], 
        zoom_start=initial_zoom)
    
    # Adicione o mapa ao container
    f = folium.Figure(width=1024, height=600)
    map.add_to(f)
    
    # Lista para armazenar todas as coordenadas 
    bounds = []

    # Adicione o MarkerCluster ao mapa
    marker_cluster = MarkerCluster().add_to(map)
    
    for index, line in df.iterrows():
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = line["rating_color_name"]
        latitude = line["latitude"]
        longitude = line["longitude"]
        
        html = f"""
        <p><h1><strong>{name}</strong></h1></p>
        <p>
            <h4><strong>Price:</strong></h4>{price_for_two},00 ({currency}) para dois</br>
            <h4><strong>Type:</strong></h4>{cuisine}</br>
            <h4><strong>Aggregate Rating:</strong></h4>{rating}/5.0
        </p>
        """
        
        popup = folium.Popup(
            folium.Html(
                html, 
                script=True), 
            max_width=500)
        
        # Adicione o marcador ao cluster
        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa")
        ).add_to(marker_cluster)

        # Adicione as coordenadas à lista de bounds
        bounds.append([latitude, longitude])
    
    # Ajuste o mapa para que todos os pontos sejam visíveis
    map.fit_bounds(bounds)

    return f
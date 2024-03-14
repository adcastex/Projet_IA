import streamlit as st
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import osmnx as ox
import geopandas as gpd
from geopy.distance import geodesic
from shapely.geometry import Point
import folium
import requests 

st.title("Cartographie")

address = st.text_input("Entrez une adresse")

api_key = "5b3ce3597851110001cf62483389841f73fd49c5a717c02d935a02e4"

def calculate_distance(source, destination, api_key):

        url = f"https://api.openrouteservice.org/v2/directions/foot-walking?api_key={api_key}&start={source}&end={destination}"

        #st.write(url)

        try:

            response = requests.get(url)

            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()

            if 'features' in data:

                route_coordinates = data['features'][0]['geometry']['coordinates']

                return route_coordinates

            else:

                return None

        except requests.RequestException as e:

            print(f"An error occurred: {e}")

            return None

if address:
    try:
        # Créer un géocodeur Nominatim
        geolocator = Nominatim(user_agent="soft")
        
        # Géolocaliser l'adresse
        location = geolocator.geocode(address)
        
        if location:
            
            user_point = Point(location.longitude, location.latitude)
            source = f"{location.longitude},{location.latitude}"
            
            user_gdf = gpd.GeoDataFrame(geometry=[user_point], crs="EPSG:4326")
            
            # Obtenir les supermarchés à partir de l'adresse
            features = ox.geometries_from_address(address, tags={'shop':'supermarket'}, dist=1000)
            
            if features.empty:
                st.error("Aucun supermarché trouvé à proximité.")
            else:
                # Convertir les données en GeoDataFrame
                gdf = gpd.GeoDataFrame.from_features(features)
                gdf['LAT'] = gdf['geometry'].centroid.y
                gdf['LON'] = gdf['geometry'].centroid.x
                gdf['tooltip'] = gdf['name'].fillna('Supermarché')
                user_location = (location.latitude, location.longitude)
                # Calculer la distance entre chaque supermarché et la position géographique de l'utilisateur
                gdf['distance'] = gdf.apply(lambda row: geodesic((location.latitude, location.longitude), (row['LAT'], row['LON'])).meters, axis=1)
                
                # Créer une liste des marques de supermarchés disponibles
                brands = ['Tous'] + gdf['brand'].unique().tolist()  # Ajouter 'Tous' à la liste
                
                # Sélectionner une marque de supermarché à l'aide d'un élément de sélection (selectbox) Streamlit
                selected_brand = st.selectbox("Sélectionner une marque de supermarché", brands)
                
                # Filtrer les supermarchés en fonction de la marque sélectionnée
                if selected_brand != 'Tous':
                    filtered_gdf = gdf[gdf['brand'] == selected_brand]
                else:
                    filtered_gdf = gdf  # Afficher tous les magasins si 'Tous' est sélectionné
                
                # Si des supermarchés sont trouvés pour la marque sélectionnée
                if not filtered_gdf.empty:
                    # Trouver le supermarché le plus proche
                    plus_proche = filtered_gdf.loc[filtered_gdf['distance'].idxmin()]
                    destination=f"{plus_proche['LON']}, {plus_proche['LAT']}"
                    
                    best_route=calculate_distance(source,destination,api_key)
                    
                    # Afficher la carte Folium
                    m = folium.Map(location=user_location, zoom_start=13)
                    
                    # Ajouter un marqueur pour chaque supermarché
                    for index, row in filtered_gdf.iterrows():
                        folium.Marker([row['LAT'], row['LON']], popup=row['tooltip']).add_to(m)
                    
                    # Ajouter un marqueur pour la position de l'utilisateur
                    folium.Marker(user_location, popup="Votre position", icon=folium.Icon(color='red')).add_to(m)
                    
                    # Ajouter un marqueur pour la localisation la plus proche en vert
                    folium.Marker([plus_proche['LAT'], plus_proche['LON']], popup=f"Plus proche : {plus_proche['name']}", icon=folium.Icon(color='green')).add_to(m)
                    
                    folium.PolyLine(locations=[(coord[1], coord[0]) for coord in best_route], color="magenta", weight=5, opacity=1).add_to(m)
                    
                    # Afficher la carte Folium
                    folium_static(m)
                    
                    # Modifier le texte en conséquence si 'Tous' est sélectionné
                    if selected_brand == 'Tous':
                        st.write(f"Le supermarché le plus proche est {plus_proche['name']} à une distance de {round(plus_proche['distance'], 2)} mètres.")
                    else:
                        st.write(f"Le supermarché le plus proche de la marque '{selected_brand}' est {plus_proche['name']} à une distance de {round(plus_proche['distance'], 2)} mètres.")
                
                else:
                    st.error(f"Aucun supermarché de la marque '{selected_brand}' trouvé à proximité.")
            
        else:
            st.error("Adresse introuvable. Veuillez entrer une adresse valide.")
        
    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

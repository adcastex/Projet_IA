import streamlit as st
from geopy.geocoders import Nominatim
import pandas as pd
import osmnx as ox
import geopandas as gpd
st.title("Cartographie")

address = st.text_input("Entrez une adresse")

if address:
    try:
        # Créer un géocodeur Nominatim
        geolocator = Nominatim(user_agent="soft")
        
        # Géolocaliser l'adresse
        location = geolocator.geocode(address)
        
        if location:
            # Affichage de la carte avec la position géolocalisée
            st.write(f"Coordonnées de l'adresse '{address}':")
            st.write("Latitude:", location.latitude)
            st.write("Longitude:", location.longitude)
            
            # Obtenir le graphe à partir du point de géolocalisation
            #supermarkets = ox.features_from_point((location.latitude, location.longitude), tags={'supermarket':True}, dist=1000)
            #supermarkets = ox.features_from_address(address, tags={'supermarket':True}, dist=1000)
            features = ox.features_from_address(address, tags={'shop':'supermarket'}, dist=1000)
            st.write(features)
            # Convertir les données en GeoDataFrame
            gdf = gpd.GeoDataFrame.from_features(features)
            gdf['LAT'] = gdf['geometry'].centroid.y
            gdf['LON'] = gdf['geometry'].centroid.x
            gdf['tooltip'] = gdf['name'].fillna('Supermarché')
            
        # Affichage de la carte avec les supermarchés à proximité
            st.map(gdf,size=5,use_container_width=True)
            for index, row in gdf.iterrows():
                st.write(f"Supermarché: {row['brand']}", row['LAT'], row['LON'])
            
        else:
            st.error("Adresse introuvable. Veuillez entrer une adresse valide.")
        
    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")
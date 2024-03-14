import streamlit as st
from PIL import Image
from geopy.geocoders import Nominatim
import pandas as pd
import osmnx as ox
import geopandas as gpd
import json




def main():
    st.set_page_config(page_title="Multipage_app")
    st.title("Piatto Pronto")
    logo = Image.open("Logo.png")
    logo_resized = logo.resize((200, 200))

    st.image(logo_resized, width=100)
    st.write("Bienvenue dans notre application ! Cette application a été réalisée durant le challenge de Web mining à la fin de notre année de Master SISE. L'objectif, est de réaliser une application IA. \n Notre application permet à nos utilisateurs de retrouver facilement des recettes de plats  vu durant leur journée.")




if __name__ == "__main__":
    main()


    

# menu = st.sidebar.radio("Navigation", ["Import image", "Affichage recette","Cartographie"])

# if menu == "Importation image":
#     st.header("Importation image")
#     image_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])
#     #if image_file is not None:
    
#         # Ouvrir l'image
#         #img = Image.open(image_file)
        
#         # Convertir l'image en tableau de pixels
#         #pixels = list(img.getdata())

#     if image_file is not None:
#         #st.write(type(image_file))
#         st.write("Image chargée avec succès :")
#         img = Image.open(image_file)
#         img_array = np.array(img)
#         #pixels = list(img.getdata())
#         st.write(img_array.shape,type(img_array))
#         st.image(image_file, caption='Image chargée', use_column_width=True)
#     else:
#         st.write("Veuillez sélectionner une image à charger.")


#     # Charger le fichier JSON
#     with open('types.json', 'r', encoding='utf-8') as file:
#         types_plats = json.load(file)

#     # Titre de l'application
#     st.title("Choix de plat")

#     # Choisir la classe (Pâtes ou Pizza)
#     classe = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=0, key=1)

#     ind=list(types_plats.keys()).index(classe)

#     class2 = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=ind, key=2)

#     # Vérifier si la classe choisie existe dans le menu
#     if class2:
#         # Afficher les types disponibles
#         types_disponibles = types_plats[class2]["types"]
#         st.write(f"Variété de recettes pour {class2} : {', '.join(types_disponibles)}")

#         # Choisir le type
#         choix_type = st.selectbox(f"Choisissez votre recette", types_disponibles)

#         # Vérifier si le type choisi existe dans la liste
#         if choix_type:
#             st.success(f"Vous avez choisi {class2} {choix_type}. Bon appétit !")
#         else:
#             st.warning("Veuillez choisir un type.")
#     else:
#         st.warning("Veuillez choisir une classe.")

# elif menu == "Affichage recette":
#     st.header("Affichage recette")

# elif menu == "map":
#     st.header("map")

#     address = st.text_input("Entrez une adresse")

#     if address:
#         try:
#             # Créer un géocodeur Nominatim
#             geolocator = Nominatim(user_agent="soft")
            
#             # Géolocaliser l'adresse
#             location = geolocator.geocode(address)
            
#             if location:
#                 # Affichage de la carte avec la position géolocalisée
#                 st.write(f"Coordonnées de l'adresse '{address}':")
#                 st.write("Latitude:", location.latitude)
#                 st.write("Longitude:", location.longitude)
                
#                 # Obtenir le graphe à partir du point de géolocalisation
#                 #supermarkets = ox.features_from_point((location.latitude, location.longitude), tags={'supermarket':True}, dist=1000)
#                 #supermarkets = ox.features_from_address(address, tags={'supermarket':True}, dist=1000)
#                 features = ox.features_from_address(address, tags={'shop':'supermarket'}, dist=1000)
#                 st.write(features)
#                 # Convertir les données en GeoDataFrame
#                 gdf = gpd.GeoDataFrame.from_features(features)
#                 gdf['LAT'] = gdf['geometry'].centroid.y
#                 gdf['LON'] = gdf['geometry'].centroid.x
#                 gdf['tooltip'] = gdf['name'].fillna('Supermarché')
                
#             # Affichage de la carte avec les supermarchés à proximité
#                 st.map(gdf,size=5,use_container_width=True)
#                 for index, row in gdf.iterrows():
#                     st.write(f"Supermarché: {row['brand']}", row['LAT'], row['LON'])
                        
#             else:
#                 st.error("Adresse introuvable. Veuillez entrer une adresse valide.")
                    
#         except Exception as e:
#             st.error(f"Une erreur s'est produite : {e}")
import streamlit as st
from PIL import Image
import numpy as np
import json
st.title("Import image")

image_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])
#if image_file is not None:
 
      # Ouvrir l'image
    #img = Image.open(image_file)
    
    # Convertir l'image en tableau de pixels
    #pixels = list(img.getdata())

if image_file is not None:
    #st.write(type(image_file))
    st.write("Image chargée avec succès :")
    img = Image.open(image_file)
    img_array = np.array(img)
    #pixels = list(img.getdata())
    st.write(img_array.shape,type(img_array))
    st.image(image_file, caption='Image chargée', use_column_width=True)
else:
    st.write("Veuillez sélectionner une image à charger.")


 


# Charger le fichier JSON
with open('types.json', 'r', encoding='utf-8') as file:
    types_plats = json.load(file)

# Titre de l'application
st.title("Choix de plat")

# Choisir la classe (Pâtes ou Pizza)
classe = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=0, key=1)

ind=list(types_plats.keys()).index(classe)

class2 = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=ind, key=2)

# Vérifier si la classe choisie existe dans le menu
if class2:
    # Afficher les types disponibles
    types_disponibles = types_plats[class2]["types"]
    st.write(f"Variété de recettes pour {class2} : {', '.join(types_disponibles)}")

    # Choisir le type
    choix_type = st.selectbox(f"Choisissez votre recette", types_disponibles)

    # Vérifier si le type choisi existe dans la liste
    if choix_type:
        st.success(f"Vous avez choisi {class2} {choix_type}. Bon appétit !")
    else:
        st.warning("Veuillez choisir un type.")
else:
    st.warning("Veuillez choisir une classe.")

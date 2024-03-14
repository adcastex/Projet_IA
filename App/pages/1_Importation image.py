import streamlit as st
from PIL import Image
import numpy as np
import json
from fonction.prediction import predi


st.title("Import image")

image_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

pred=' '


if image_file is not None:

    st.write("Image chargée avec succès :")

    img = Image.open(image_file)

    img_array = np.array(img)

    st.image(image_file, caption='Image chargée', use_column_width=True)

    pred=predi(img_array)

    print("########################"+pred)

else:
    st.write("Veuillez sélectionner une image à charger.")


# Charger le fichier JSON
with open('types.json', 'r', encoding='utf-8') as file:
    types_plats = json.load(file)

# Titre de l'application
st.title("Choix de plat")

if(pred==" "):
    ind=0

else:
    st.write("Le plat que vous voulez manger est a base de: "+pred)
    ind=list(types_plats.keys()).index(pred)


# Choisir la classe (Pâtes ou Pizza)
classe = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=ind, key=1)

# Vérifier si la classe choisie existe dans le menu
if classe:
    # Afficher les types disponibles
    types_disponibles = types_plats[classe]["types"]
    st.write(f"Variété de recettes pour {classe} : {', '.join(types_disponibles)}")

    # Choisir le type
    choix_type = st.selectbox(f"Choisissez votre recette", types_disponibles)

    # Vérifier si le type choisi existe dans la liste
    if choix_type:
        st.success(f"Vous avez choisi {classe} {choix_type}. Bon appétit !")
    else:
        st.warning("Veuillez choisir un type.")
else:
    st.warning("Veuillez choisir une classe.")

import streamlit as st
from PIL import Image
import numpy as np
import json
from fonction.prediction import predi
from fonction.recette import Marmiton, search_and_display_recipe
import os 

st.title("Recette")

pred=' '

# # Onglets
# onglet_selectionne = st.sidebar.radio("Navigation", ["Importation image", "Affichage recette", "map"])


# if onglet_selectionne == "Affichage recette":
    
st.header("Affichage recette")
# Ajoutez ici le contenu de votre onglet
image_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

# pred=' '


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


if(pred==" "):
    ind=0
else:
    st.write("Le plat que vous voulez manger est à base de: "+pred)
    ind=list(types_plats.keys()).index(pred)

classe = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=ind, key=1)

# Vérifier si la classe choisie existe dans le menu
if classe:
    # Afficher les types disponibles
    types_disponibles = types_plats[classe]["types"]
    #st.write(f"Variété de recettes pour {class2} : {', '.join(types_disponibles)}")

    # Choisir le type
    choix_type = st.text_input(f"Entrez le type de recette que vous recherchez", "")
    print("#####################################",os.listdir())
    if choix_type:
        # Convertir le type de recette en mot-clé correspondant à la recette sur Marmiton
        mot_cle = classe
        # Afficher le mot-clé correspondant
        #st.info(f"Les mot-clés correspondant à votre recette est : {mot_cle} {choix_type}")
        choix_type=choix_type+" "+mot_cle
        # Appeler la fonction search_and_display_recipe avec les mots-clés
        recipe_data = search_and_display_recipe(keywords=f'{choix_type}')
        # Afficher les caractéristiques de la recette
        if recipe_data:
            st.subheader(f"🥘 **Une recette de {recipe_data.get('name', 'Non spécifié')}** : ")
            #st.write(f"Nom de la recette: {recipe_data.get('name', 'Non spécifié')}")
            st.info("📋 **Ingrédients:**")
            for ingredient in recipe_data.get('ingredients', []):
                st.write(f"- {ingredient}")
            st.info(f"⏱️ **Temps de préparation: {recipe_data.get('total_time', 'Non spécifié')}**")
            st.info(f"💰 **Budget: {recipe_data.get('budget', 'Non spécifié')}**")
            st.info(" 🔪 **Étapes de préparation:**")
            for idx, step in enumerate(recipe_data.get('steps', []), start=1):
                st.write(f"{idx}. {step}")
        else:
            st.warning("Aucune recette trouvée pour les mots-clés saisis.")
    
    else:
        st.warning("Veuillez choisir un type.")
else:
    st.warning("Veuillez choisir une classe.")






# st.title("Import image")

# image_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

# pred=' '


# if image_file is not None:

#     st.write("Image chargée avec succès :")

#     img = Image.open(image_file)

#     img_array = np.array(img)

#     st.image(image_file, caption='Image chargée', use_column_width=True)

#     pred=predi(img_array)

#     print("########################"+pred)

# else:
#     st.write("Veuillez sélectionner une image à charger.")


# # Charger le fichier JSON
# with open('types.json', 'r', encoding='utf-8') as file:
#     types_plats = json.load(file)

# # Titre de l'application
# st.title("Choix de plat")

# if(pred==" "):
#     ind=0

# else:
#     st.write("Le plat que vous voulez manger est a base de: "+pred)
#     ind=list(types_plats.keys()).index(pred)


# # Choisir la classe (Pâtes ou Pizza)
# classe = st.selectbox("Choisissez une classe", list(types_plats.keys()), index=ind, key=1)

# # Vérifier si la classe choisie existe dans le menu
# if classe:
#     # Afficher les types disponibles
#     types_disponibles = types_plats[classe]["types"]
#     st.write(f"Variété de recettes pour {classe} : {', '.join(types_disponibles)}")

#     # Choisir le type
#     choix_type = st.selectbox(f"Choisissez votre recette", types_disponibles)

#     # Vérifier si le type choisi existe dans la liste
#     if choix_type:
#         st.success(f"Vous avez choisi {classe} {choix_type}. Bon appétit !")
#     else:
#         st.warning("Veuillez choisir un type.")
# else:
#     st.warning("Veuillez choisir une classe.")

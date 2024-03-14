import streamlit as st
from PIL import Image
# Entête
def main():
    st.set_page_config(page_title="Multipage_app")
    st.title("Application de détection de plat et affichage de la recette")
    st.write("Bienvenue dans notre application ! Cette application a pour objectif de vous proposez des recettes du plat en fonction de l'image importé et la localisation des supermarchés ou vous rendre si besoin pour acheter vos ingrédients. Nous vous invitons à explorez les différents onglets.")
    logo = Image.open("App/Logo.png")

# Redimensionner l'image du logo
    logo_resized = logo.resize((200, 200))

# Afficher le logo centré
    st.image(logo_resized, width=400)
if __name__ == "__main__":
    main()
# Onglets
menu = st.sidebar.selectbox(
    "Navigation",
    ("Importation image", "Affichage recette", "map")
)

# Contenu de chaque onglet
if menu == "Importation image":
    st.header("Importation image")
    # Ajoutez ici le contenu de votre premier onglet
elif menu == "Affichage recette":
    st.header("Affichage recette")
    # Ajoutez ici le contenu de votre deuxième onglet
elif menu == "map":
    st.header("map")
    # Ajoutez ici le contenu de votre troisième onglet
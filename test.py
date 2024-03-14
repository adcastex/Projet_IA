import streamlit as st

# Ajouter des onglets à la barre latérale
onglet_selectionne = st.sidebar.radio("Navigation", ["Page 1", "Page 2"])

# Afficher le contenu en fonction de l'onglet sélectionné
if onglet_selectionne == "Page 1":
    st.subheader("Page 1")
    st.write("Contenu de la page 1 ici...")
elif onglet_selectionne == "Page 2":
    st.subheader("Page 2")
    st.write("Contenu de la page 2 ici...")
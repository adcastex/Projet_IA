import streamlit as st
import time

def afficher_chronometre(ss):
    temps_ecoule = int(time.time() - ss)
    heures = temps_ecoule // 3600
    minutes = (temps_ecoule % 3600) // 60
    secondes = temps_ecoule % 60
    st.write(f"Temps écoulé : {heures:02}:{minutes:02}:{secondes:02}")


st.title("Chronomètre")

if("start" not in st.session_state):
    st.session_state.start = 0
st.write(st.session_state.start)
start_button = st.button("Démarrer")
reset_button = st.button("Réinitialiser")

if start_button:
    st.session_state.start = time.time()

if reset_button:
    st.session_state.start = 0

if st.session_state.start !=0:
    afficher_chronometre(st.session_state.start)

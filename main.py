import numpy as np
import streamlit as st
import pandas as pd
import csv
import requests
from datetime import datetime
# Configuration de la page

st.set_page_config(
    layout="wide", page_title="Dunkball - Terrains de basket", page_icon=":basketball:")

# Titre de l'application
st.title(":basketball: Dunkball", anchor=False)
st.subheader("Liste des terrains de basket")

# Lecture du fichier CSV
API_KEY = "AIzaSyBF1ttSNSKP2Ylz3SuGAaAc1T8G5cZ5e6A"

# url csv https://docs.google.com/spreadsheets/d/e/2PACX-1vTim8FmmeIWAEc2c70WoA3wRZeRePAQkWQE8jRq3_OQvDQyfgQSWHhsiFRRsPgdZCEdt1gTV0WUdcHN/pub?output=csv


@st.cache_data(ttl=600, show_spinner="Chargement des données...")
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTim8FmmeIWAEc2c70WoA3wRZeRePAQkWQE8jRq3_OQvDQyfgQSWHhsiFRRsPgdZCEdt1gTV0WUdcHN/pub?output=csv"
    response = requests.get(url)
    reader = list(csv.reader(response.text.splitlines()))
    headers = reader[0]
    data = reader[1:]
    st.caption(
        f"Données mise à jour à {datetime.now().strftime('%H:%M:%S')}")
    return [dict(zip(headers, row)) for row in data]


# Chargement des données
terrains = load_data()


def afficher_terrains(terrains):
    # Affichage des terrains
    for terrain_data in terrains:
        terrain = {
            'nom': terrain_data['Nom'],
            'ville': terrain_data['Ville'],
            'etat': terrain_data['Etat'],
            'latitude': terrain_data['Latitude'],
            'longitude': terrain_data['Longitute'],
            'nombre_de_paniers': terrain_data['nombre de panier'],
            'commentaire': terrain_data['commentaire'].strip(),
            'type_city': terrain_data['type city'],
            'arceaux_simple': terrain_data['arrseaux simple'],
            'arceaux_double': terrain_data['arrseaux double'],
            'arceaux_prolonger': terrain_data['arrseaux prolonger'],
            'adresse': terrain_data['Adresse'],
            'code_postal': terrain_data['Code Postal']
        }
        main = st.empty()
        with st.container(border=True):
            if st.button(terrain['nom'], type="tertiary"):
                afficher_terrain(terrain)
            st.caption(
                f"{terrain['etat']} - {terrain['ville']} - {terrain['nombre_de_paniers']} paniers")

    if st.button("Rafraîchir les données"):
        main.empty()
        load_data.clear()
        st.rerun()


@st.dialog(title="Informations sur le terrain", width="large")
def afficher_terrain(terrain):

    st.subheader(f"🏀 {terrain['nom']}")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"{terrain['adresse']}")
        st.write(f"{terrain['ville']} {terrain['code_postal']}")
        st.write(f"**État:** {terrain['etat']}")
        st.metric(
            f"**Nombre de paniers:**", terrain['nombre_de_paniers'])
        # st.write("**Latitude:**", latitude)
        # st.write("**Longitude:**", longitude)
    st.markdown(f"""<iframe
    width="450"
    height="250"
    frameborder="0" style="border:0"
    referrerpolicy="no-referrer-when-downgrade"
    src="https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={terrain['latitude']}, {terrain['longitude']}"
    allowfullscreen>
    </iframe>""", unsafe_allow_html=True)

    with col2:
        st.write("**Type city:**",
                 "Oui" if terrain['type_city'] == 2 else "Non")
        st.metric("**Arceaux simples:**", terrain['arceaux_simple'])
        st.metric("**Arceaux doubles:**", terrain['arceaux_double'])
        st.metric("**Arceaux prolongés:**", terrain['arceaux_prolonger'])

    if terrain['commentaire']:
        st.info(f"💬 Commentaire: {terrain['commentaire']}")


afficher_terrains(terrains)

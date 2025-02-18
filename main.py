import csv  # on utilise le module csv qui est deja dans python
import streamlit as st
import requests

# on va stocker nos terrains dans une liste


def lire_fichier_csv():
    liste_terrains = []
    print("Je commence à lire le fichier...")
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTim8FmmeIWAEc2c70WoA3wRZeRePAQkWQE8jRq3_OQvDQyfgQSWHhsiFRRsPgdZCEdt1gTV0WUdcHN/pub?output=csv"
    response = requests.get(url)
    lecteur = list(csv.reader(response.text.splitlines()))
    n = 0
    # pour chaque ligne du fichier
    for ligne in lecteur:
        # on saute la premiere ligne qui contient les noms des collonnes
        if n > 0:
            # on ajoute le terrain à notre liste
            terrain = {
                'nom': ligne[0],
                'adresse': ligne[1],
                'code_postal': ligne[2],
                'ville': ligne[3],
                'latitude': ligne[4],
                'longitude': ligne[5],
                'etat': ligne[6],
                'nombre_de_paniers': ligne[7],
                'type_city': ligne[8],
                'arceaux_simple': ligne[9],
                'arceaux_double': ligne[10],
                'arceaux_prolonger': ligne[11],
                'commentaire': ligne[12].strip(),
            }
            liste_terrains.append(terrain)
        n += 1
    return liste_terrains


def afficher_terrains(terrains):
    # Affichage des terrains
    for terrain in terrains:
        with st.container(border=True):
            if st.button(terrain['nom'], type="tertiary"):
                afficher_terrain(terrain)
            st.caption(
                f"{terrain['etat']} - {terrain['ville']} - {terrain['nombre_de_paniers']} paniers")


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

    st.markdown(f"""<iframe
    width="450"
    height="250"
    frameborder="0" style="border:0"
    referrerpolicy="no-referrer-when-downgrade"
    src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBF1ttSNSKP2Ylz3SuGAaAc1T8G5cZ5e6A&q={terrain['latitude']}, {terrain['longitude']}"
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


st.set_page_config(
    layout="wide", page_title="Dunkball - Terrains de basket", page_icon=":basketball:")

# Titre de l'application
st.title(":basketball: Dunkball", anchor=False)
st.subheader("Liste des terrains de basket")
liste_terrains = lire_fichier_csv()
afficher_terrains(liste_terrains)

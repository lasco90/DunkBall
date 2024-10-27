import csv  # on utilise le module csv qui est deja dans python
import streamlit as st

# on va stocker nos terrains dans une liste


def lire_fichier_csv():
    liste_terrains = []
    print("Je commence à lire le fichier...")
    with open('terrains.csv', 'r', encoding='utf-8') as fichier:
        # on utilise reader qui va nous donner des listes
        lecteur = csv.reader(fichier)

        n = 0
        # pour chaque ligne du fichier
        for ligne in lecteur:
            # on saute la premiere ligne qui contient les noms des collonnes
            if n > 0:
                # on ajoute le terrain à notre liste
                liste_terrains.append(ligne)
            n += 1
    return liste_terrains


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


    with col2:

        st.write("**Type city:**",
                 "Oui" if terrain['type_city'] == 2 else "Non")
        st.metric("**Arceaux simples:**", terrain['arceaux_simple'])
        st.metric("**Arceaux doubles:**", terrain['arceaux_double'])
        st.metric("**Arceaux prolongés:**", terrain['arceaux_prolonger'])

    if terrain['commentaire']:
        st.info(f"💬 Commentaire: {terrain['commentaire']}")


liste_terrains = lire_fichier_csv()
afficher_terrains(terrains)
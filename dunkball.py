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


liste_terrains = lire_fichier_csv()
# Affichage des informations dans Streamlit
if liste_terrains:
    st.title("Terrains de basket")

    # Affichage du premier terrain
    st.subheader("Premier terrain de la liste")
    st.write(f"Nom: {liste_terrains[0][0]}")
    st.write(f"Adresse: {liste_terrains[0][1]}")
    st.write(f"Ville: {liste_terrains[0][3]}")

    # Affichage du nombre total de terrains
    st.subheader("Statistiques")
    st.write(f"Nombre total de terrains : {len(liste_terrains)}")

    # Affichage de la liste des terrains
    st.subheader("Liste de tous les terrains")
    for terrain in liste_terrains:
        st.write(f"- {terrain[0]}")
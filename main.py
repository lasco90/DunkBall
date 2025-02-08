import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Dunkball - Terrains de basket", layout="wide")

# Titre de l'application
st.title("Dunkball")
st.subheader("Liste des terrains de basket")

# Lecture du fichier CSV


def load_data():
    df = pd.read_csv('terrains.csv')
    return df


# Chargement des données
df = load_data()


# Filtres
col1, col2 = st.columns(2)

with col1:
    # Filtre par ville
    villes = ['Toutes les villes'] + sorted(df['Ville'].unique().tolist())
    ville_selectionnee = st.selectbox('Filtrer par ville:', villes)

with col2:
    # Filtre par état
    etats = ['Tous les états'] + sorted(df['Etat'].unique().tolist())
    etat_selectionne = st.selectbox('Filtrer par état:', etats)

# Application des filtres
filtered_df = df.copy()
if ville_selectionnee != 'Toutes les villes':
    filtered_df = filtered_df[filtered_df['Ville'] == ville_selectionnee]
if etat_selectionne != 'Tous les états':
    filtered_df = filtered_df[filtered_df['Etat'] == etat_selectionne]

# Affichage des terrains
for _, terrain in filtered_df.iterrows():
    with st.expander(f"🏀 {terrain['Nom']} - {terrain['Ville']}"):

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Adresse:**", terrain['Adresse'])
            st.write("**Code Postal:**", terrain['Code Postal'])
            st.write("**État:**", terrain['Etat'])
            st.write("**Nombre de paniers:**", terrain['nombre de panier'])

        with col2:
            st.write("**Type city:**",
                     "Oui" if terrain['type city'] == 2 else "Non")
            st.write("**Arceaux simples:**", terrain['arrseaux simple'])
            st.write("**Arceaux doubles:**", terrain['arrseaux double'])
            st.write("**Arceaux prolongés:**", terrain['arrseaux prolonger'])

        if not pd.isna(terrain['commentaire']):
            st.info(f"💬 Commentaire: {terrain['commentaire']}")

# Affichage des statistiques
st.sidebar.header("Statistiques")
st.sidebar.metric("Nombre total de terrains", len(df))
st.sidebar.metric("Nombre de terrains affichés", len(filtered_df))
st.sidebar.metric("Nombre total de paniers",
                  filtered_df['nombre de panier'].sum())

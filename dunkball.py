import csv  # on utilise le module csv qui est deja dans python

# on va stocker nos terrains dans une liste
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

# on affiche le premier terrain pour voir à quoi ça ressemble
print("\nVoici le premier terrain de la liste :")
print(f"Nom: {liste_terrains[0][0]}")
print(f"Adresse: {liste_terrains[0][1]}")
print(f"Ville: {liste_terrains[0][3]}")

# on affiche le nombre total de terrains
print(f"\nNombre total de terrains : {len(liste_terrains)}")

# on affiche tous les noms des terrains
print("\nListe de tous les terrains :")
for terrain in liste_terrains:
    print(f"- {terrain[0]}")  # le nom est dans la première colonne (index 0)

import random

# Fonction pour afficher la grille de jeu
def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille, symbole):
    for i in range(3):
        if all([case == symbole for case in grille[i]]):  # Vérifie les lignes
            return True
        if all([grille[j][i] == symbole for j in range(3)]):  # Vérifie les colonnes
            return True
    # Vérifie les diagonales
    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole:
        return True
    if grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole:
        return True
    return False

# Fonction pour vérifier si la grille est pleine (match nul)
def grille_pleine(grille):
    for ligne in grille:
        if "" in ligne:
            return False
    return True

# Fonction de l'IA pour choisir une case
def ia(grille, signe):
    # Choisit une case libre aléatoire
    cases_libres = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == ""]
    if cases_libres:
        ligne, colonne = random.choice(cases_libres)
        grille[ligne][colonne] = signe
        print(f"L'IA joue en case {(ligne * 3 + colonne + 1)}")
        afficher_grille(grille)

# Fonction principale du jeu
def jouer():
    # Initialiser une grille vide
    grille = [["" for _ in range(3)] for _ in range(3)]
    joueur = "X"
    ia_signe = "O"

    print("Bienvenue dans le jeu Tic Tac Toe contre l'IA !")
    afficher_grille(grille)

    while True:
        # Tour du joueur
        if joueur == "X":
            print("\nC'est votre tour !")
            try:
                choix = int(input("Choisissez une case (1 à 9) : ")) - 1
                ligne, colonne = choix // 3, choix % 3

                if grille[ligne][colonne] == "":
                    grille[ligne][colonne] = joueur
                    afficher_grille(grille)

                    # Vérifie si le joueur gagne
                    if verifier_victoire(grille, joueur):
                        print("Félicitations ! Vous avez gagné !")
                        break
                    elif grille_pleine(grille):
                        print("Match nul ! La grille est pleine.")
                        break

                    # Passe au tour de l'IA
                    joueur = ia_signe
                else:
                    print("Cette case est déjà prise, veuillez en choisir une autre.")
            except (IndexError, ValueError):
                print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9.")
        
        # Tour de l'IA
        else:
            print("\nTour de l'IA...")
            ia(grille, ia_signe)

            # Vérifie si l'IA gagne
            if verifier_victoire(grille, ia_signe):
                print("L'IA a gagné !")
                break
            elif grille_pleine(grille):
                print("Match nul ! La grille est pleine.")
                break

            # Passe au tour du joueur
            joueur = "X"

# Lancer le jeu
if __name__ == "__main__":
    jouer()


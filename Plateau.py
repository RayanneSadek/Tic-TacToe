# Initialisation du plateau
def afficher_plateau(plateau):
    for i in range(3):
        print(f" {plateau[i*3]} | {plateau[i*3+1]} | {plateau[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print()

# Vérification de la victoire
def verifier_victoire(plateau, joueur):
    # Vérifications des lignes, colonnes et diagonales
    for i in range(3):
        # Lignes
        if plateau[i*3] == plateau[i*3+1] == plateau[i*3+2] == joueur:
            return True
        # Colonnes
        if plateau[i] == plateau[i+3] == plateau[i+6] == joueur:
            return True
    # Diagonales
    if plateau[0] == plateau[4] == plateau[8] == joueur:
        return True
    if plateau[2] == plateau[4] == plateau[6] == joueur:
        return True
    return False

# Vérification de l'égalité (match nul)
def verifier_match_nul(plateau):
    return all(c == 'X' or c == 'O' for c in plateau)

# Fonction principale du jeu
def morpion():
    plateau = [' ']*9  # Liste représentant les 9 cases du plateau (vide au début)
    joueur_actuel = 'X'
    
    while True:
        afficher_plateau(plateau)
        print(f"C'est au tour de {joueur_actuel}.")
        
        # Demande à l'utilisateur de choisir une case
        choix = -1
        while choix < 0 or choix > 8 or plateau[choix] != ' ':
            try:
                choix = int(input(f"Choisissez une case (0-8): "))
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        
        plateau[choix] = joueur_actuel  # Le joueur joue dans la case choisie
        
        # Vérifier si le joueur actuel a gagné
        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur_actuel} a gagné !")
            break
        
        # Vérifier si c'est un match nul
        if verifier_match_nul(plateau):
            afficher_plateau(plateau)
            print("C'est un match nul !")
            break
        
        # Changer de joueur
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

# Démarrer le jeu
if __name__ == "__main__":
    morpion()

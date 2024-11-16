def afficher_plateau(plateau): 
    for i in range(3):
        print(f" {plateau[i*3]} | {plateau[i*3+1]} | {plateau[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print()

def verifier_victoire(plateau, joueur):
    for i in range(3):
        if plateau[i*3] == plateau[i*3+1] == plateau[i*3+2] == joueur:
            return True # Lignes
        if plateau[i] == plateau[i+3] == plateau[i+6] == joueur:
            return True  # Colonnes
    if plateau[0] == plateau[4] == plateau[8] == joueur:
        return True # Diagonale 1
    if plateau[2] == plateau[4] == plateau[6] == joueur:
        return True # Diagonale 2
    return False

def verifier_match_nul(plateau):
    return all(c == 'X' or c == 'O' for c in plateau)

# Fonction pour l'IA
def ia(plateau, signe):
    adversaire = 'O' if signe == 'X' else 'X'
    
    # Vérifier si l'IA peut gagner
    for i in range(9):
        if plateau[i] == ' ':
            plateau[i] = signe
            if verifier_victoire(plateau, signe):
                return i
            plateau[i] = ' '  # Annuler le mouvement
    
    # Bloquer le coup gagnant de l'adversaire
    for i in range(9):
        if plateau[i] == ' ':
            plateau[i] = adversaire
            if verifier_victoire(plateau, adversaire):
                plateau[i] = ' '  # Annuler le mouvement
                return i
            plateau[i] = ' '  # Annuler le mouvement
    
    # Jouer au centre si possible
    if plateau[4] == ' ':
        return 4
    
    # Jouer dans un coin libre
    for i in [0, 2, 6, 8]:
        if plateau[i] == ' ':
            return i
    
    # Jouer sur une case libre restante
    for i in range(9):
        if plateau[i] == ' ':
            return i

# Fonction principale du jeu
def morpion():
    plateau = [' ']*9
    joueur_actuel = 'X'
    
    while True:
        afficher_plateau(plateau)
        print(f"C'est au tour de {joueur_actuel}.")
        
        if joueur_actuel == 'X':
            # Tour du joueur humain
            choix = -1
            while choix < 0 or choix > 8 or plateau[choix] != ' ':
                try:
                    choix = int(input(f"Choisissez une case (0-8): "))
                except ValueError:
                    print("Veuillez entrer un nombre entier valide.")
        else:
            # Tour de l'IA
            choix = ia(plateau, joueur_actuel)
            print(f"L'IA choisit la case {choix}.")
        
        plateau[choix] = joueur_actuel
        
        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur_actuel} a gagné !")
            break
        
        if verifier_match_nul(plateau):
            afficher_plateau(plateau)
            print("C'est un match nul !")
            break
        
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

# Démarrer le jeu
if __name__ == "__main__":
    morpion()

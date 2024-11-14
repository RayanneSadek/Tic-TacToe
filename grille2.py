from colorama import init, Fore, Back, Style
# Importe les modules nécessaires de colorama pour gérer les couleurs dans la console

# Initialiser colorama
init(autoreset=True)
# Initialise colorama avec autoreset=True pour réinitialiser les couleurs après chaque utilisation

def afficher_grille(grille):
    # Définit une fonction pour afficher la grille du jeu Tic Tac Toe
    """
    Affiche la grille de jeu Tic Tac Toe avec un style ASCII simple et des couleurs.
    """
    # Docstring expliquant le but de la fonction

    print(f"\n{Fore.YELLOW}+---+---+---+")
    # Affiche la ligne supérieure de la grille en jaune

    for i, rangee in enumerate(grille):
        # Boucle à travers chaque rangée de la grille
        print(f"{Fore.YELLOW}|", end="")
        # Affiche le bord gauche de la rangée en jaune
        for case in rangee:
            # Boucle à travers chaque case de la rangée
            if case == "X":
                # Si la case contient un X
                print(f"{Fore.RED} {case} {Fore.YELLOW}|", end="")
                # Affiche le X en rouge, suivi d'une barre verticale jaune
            elif case == "O":
                # Si la case contient un O
                print(f"{Fore.GREEN} {case} {Fore.YELLOW}|", end="")
                # Affiche le O en vert, suivi d'une barre verticale jaune
            else:
                # Si la case est vide ou contient autre chose
                print(f"{Fore.WHITE} {case} {Fore.YELLOW}|", end="")
                # Affiche le contenu en blanc, suivi d'une barre verticale jaune
        print(f"\n{Fore.YELLOW}+---+---+---+")
        # Affiche la ligne horizontale inférieure de chaque rangée en jaune

# Exemple d'utilisation
grille = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", " ", "O"]]
# Crée une grille exemple avec des X, des O et un espace vide

afficher_grille(grille)
# Appelle la fonction afficher_grille avec la grille exemple
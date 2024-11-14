import random
from colorama import init, Fore, Back, Style

# Initialiser colorama
init(autoreset=True)

def print_board(board):
    """Affiche le plateau de jeu avec des couleurs."""
    print(f"\n{Fore.CYAN}=== Plateau de Jeu ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}+---+---+---+")
    for row in board:
        print(f"{Fore.YELLOW}|", end="")
        for cell in row:
            if cell == "X":
                print(f"{Fore.RED} {cell} {Fore.YELLOW}|", end="")
            elif cell == "O":
                print(f"{Fore.GREEN} {cell} {Fore.YELLOW}|", end="")
            else:
                print(f"{Fore.WHITE} {cell} {Fore.YELLOW}|", end="")
        print(f"\n{Fore.YELLOW}+---+---+---+")

def player_move(board, player):
    """Gère le mouvement d'un joueur."""
    while True:
        try:
            move = input(f"{Fore.YELLOW}Joueur {player}, entrez votre coup (ligne,colonne): {Style.RESET_ALL}")
            row, col = map(int, move.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == " ":
                board[row-1][col-1] = player
                break
            else:
                print(f"{Fore.RED}Coup non valide. Veuillez réessayer.{Style.RESET_ALL}")
        except (ValueError, IndexError):
            print(f"{Fore.RED}Saisie invalide. Utilisez le format 'ligne,colonne' (ex: 2,3).{Style.RESET_ALL}")

def check_win(board):
    """Vérifie s'il y a un gagnant."""
    lines = (
        board +  # lignes horizontales
        list(map(list, zip(*board))) +  # lignes verticales
        [[board[i][i] for i in range(3)]] +  # diagonale principale
        [[board[i][2-i] for i in range(3)]]  # diagonale secondaire
    )
    return any(line.count(line[0]) == 3 and line[0] != " " for line in lines)

def check_tie(board):
    """Vérifie s'il y a égalité."""
    return all(cell != " " for row in board for cell in row)

def play_game():
    """Fonction principale du jeu."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice(["X", "O"])
    
    print(f"{Fore.MAGENTA}=== Bienvenue au Tic Tac Toe ! ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}Le joueur {current_player} commence.{Style.RESET_ALL}")

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board):
            print_board(board)
            print(f"{Fore.GREEN}Le joueur {current_player} gagne !{Style.RESET_ALL}")
            break
        if check_tie(board):
            print_board(board)
            print(f"{Fore.YELLOW}Match nul !{Style.RESET_ALL}")
            break

        current_player = "O" if current_player == "X" else "X"

    print(f"\n{Fore.MAGENTA}=== Fin de la partie ! ==={Style.RESET_ALL}")

if __name__ == "__main__":
    play_game()
def afficher_grille(grille):

    print("\n╔═══╦═══╦═══╗")
    for i, rangee in enumerate(grille):
        print("║", end=" ")
        for j, case in enumerate(rangee):
            print(f"{case:^3}", end="")
            if j < 2:
                print("║", end=" ")
        print("║")
        if i < 2:
            print("╠═══╬═══╬═══╣")
            
    print("╚═══╩═══╩═══╝")
def afficher_tapis(n):
    bordure = "+" + "-"*(n+1) + "+"
    print(bordure)
    for i in range(n+1):
        ligne = "|"
        for j in range(n+1):
            if i + j == n:
                ligne += " "
            else:
                ligne += "#"
        ligne += "|"
        print(ligne)
    print(bordure)

afficher_tapis(10)
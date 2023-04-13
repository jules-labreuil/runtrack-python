def Produits_disponibles(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise et cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour et endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine et navet")
    else:
        print("Aucun produit correspondant à votre recherche")

Produits_disponibles("fruits", "hiver")
Produits_disponibles("fruits", "été")
Produits_disponibles("légumes", "hiver")
Produits_disponibles("légumes", "été")
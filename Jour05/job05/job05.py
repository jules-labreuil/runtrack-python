def distance_toilettes(marches, hauteur):
    distance = marches * hauteur * 2 * 5 / 100
    distance_km = distance / 1000
    return "Pour {} marches de {} cm, le gardien parcourt {:.2f} km par semaine.".format(marches, hauteur, distance_km)

print(distance_toilettes(100, 20))
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
sum_paires = 0

for x in L:
    if x % 2 == 0:
        sum_paires += x

print("La somme de toutes les valeurs paires de la liste est:", sum_paires)
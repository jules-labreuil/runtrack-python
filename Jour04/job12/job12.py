def tri_liste(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    return liste

ma_liste = [15, 16, 54, 8, 67]
tri_liste(ma_liste)
print(ma_liste)
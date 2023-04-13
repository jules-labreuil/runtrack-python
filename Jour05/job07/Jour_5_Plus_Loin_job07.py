def changer_mot(mot):
  
    if not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres de l'alphabet.")
        
        return mot
    
    lettres = list(mot)
    
    for i in range(len(lettres)-1):
        if ord(lettres[i]) > ord(lettres[i+1]):
            lettres[i], lettres[i+1] = lettres[i+1], lettres[i]
            lettres[i+1:] = sorted(lettres[i+1:])

            return ''.join(lettres)
    
    return mot

mot = input("Entrez un mot sans espace ni aucun autre caractère que les 26 lettres de l’alphabet : ")

nouveau_mot = changer_mot(mot)

# Afficher le nouveau mot
print("Le nouveau mot est :", nouveau_mot)
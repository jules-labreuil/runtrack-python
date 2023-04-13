def changer_mot(mot):
    # Vérifier que le mot ne contient que des lettres
    if not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres de l'alphabet.")
        return mot
    
    # Convertir le mot en une liste de lettres
    lettres = list(mot)
    
    # Trouver la première paire de lettres consécutives qui ne sont pas dans l'ordre alphabétique
    for i in range(len(lettres)-1):
        if ord(lettres[i]) > ord(lettres[i+1]):
            # Échanger ces lettres
            lettres[i], lettres[i+1] = lettres[i+1], lettres[i]
            
            # Replacer les lettres suivantes dans l'ordre alphabétique
            lettres[i+1:] = sorted(lettres[i+1:])
            
            # Convertir la liste de lettres en un mot et le retourner
            return ''.join(lettres)
    
    # Si toutes les lettres sont déjà dans l'ordre alphabétique, retourner le mot original
    return mot

# Demander le mot à l'utilisateur
mot = input("Entrez un mot sans espace ni aucun autre caractère que les 26 lettres de l’alphabet : ")

# Changer le mot en un nouveau mot "plus loin" dans l'ordre alphabétique
nouveau_mot = changer_mot(mot)

# Afficher le nouveau mot
print("Le nouveau mot est :", nouveau_mot)
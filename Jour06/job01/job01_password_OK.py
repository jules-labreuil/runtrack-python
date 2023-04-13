import re
import hashlib

while True:
    password = input("Veuillez entrer votre mot de passe :")

    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue

    if not re.search("[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        continue

    if not re.search("[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue

    if not re.search("[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue

    if not re.search("[!@#$%^&*€]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        continue

    hash_object = hashlib.sha256(password.encode())
    print("Mot de passe valide !")
    print("Le mot de passe encrypté est :", hash_object.hexdigest())
    break
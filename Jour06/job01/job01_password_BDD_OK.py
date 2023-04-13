import hashlib
import json
import re
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FILENAME = "passwords.json"

DB_PATH = os.path.join(BASE_DIR, FILENAME)

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump({}, f)

def reset_passwords():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"La base de données {FILENAME} a été réinitialisée.")
    else:
        print(f"La base de données {FILENAME} n'existe pas.")

def compare_passwords(password1, password2):
    return password1 == password2

def add_password():
    website = input("Entrez le nom du site web : ")
    username = input("Entrez votre nom d'utilisateur : ")

    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({}, f)

    with open(DB_PATH, "r") as f:
        passwords = json.load(f)

    if website in passwords and username in passwords[website]:
        print("Un mot de passe pour ce site web et cet identifiant existe déjà.")
        return

    password = input("Entrez votre mot de passe : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    while True:
        if len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
        elif not re.search("[A-Z]", password):
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not re.search("[a-z]", password):
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not re.search("[0-9]", password):
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not re.search("[!@#$%^&*]", password):
            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            break
        password = input("Entrez votre mot de passe : ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for site in passwords:
        for user in passwords[site]:
            if compare_passwords(hashed_password, passwords[site][user]):
                print("Mot de passe déjà utilisé par un autre profil.")
                password = input("Entrez un nouveau mot de passe : ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                break

    if website not in passwords:
        passwords[website] = {}
    passwords[website][username] = hashed_password
    print("Nouveau mot de passe ajouté avec succès !")

    with open(DB_PATH, "w") as f:
        json.dump(passwords, f)

def view_passwords():
    try:
        with open(DB_PATH, "r") as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = {}

    if len(passwords) == 0:
        print("Aucun mot de passe enregistré.")
    else:
        for website, data in passwords.items():
            print("Site web :", website)
            for username, password in data.items():
                print("Nom d'utilisateur :", username)
                print("Mot de passe :", password)
                print("-" * 20)

while True:
    print("Que voulez-vous faire ?")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher les mots de passe enregistrés")
    print("3. Réinitialiser la base de données")
    print("4. Quitter le programme")

    choice = input("Entrez votre choix (1, 2, 3 ou 4) : ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        reset_passwords()
    elif choice == "4":
        break
    else:
        print("Choix non valide")
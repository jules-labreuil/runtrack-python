import hashlib
import re
import os
import select
import sys
import tkinter as tk
import json

# Chemin vers la base de données
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

FILENAME = "passwords.json"

DB_PATH = os.path.join(BASE_DIR, FILENAME)

if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        json.dump({}, f)

def is_input_ready():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def reset_passwords():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"La base de données {FILENAME} a été réinitialisée.")
    else:
        print(f"La base de données {FILENAME} n'existe pas.")

def compare_passwords(password1, password2):
    return password1 == password2

def add_password():
    # Désactive les boutons
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    button4.config(state="disabled")

    website = input("Entrez le nom du site web : ")
    username = input("Entrez votre nom d'utilisateur : ")

    with open(DB_PATH, "r") as f:
        passwords = json.load(f)

    if website in passwords and username in passwords[website]:
        print("Un mot de passe pour ce site web et cet identifiant existe déjà.")
        # Réactive les boutons
        button1.config(state="normal")
        button2.config(state="normal")
        button3.config(state="normal")
        button4.config(state="normal")
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

    # Réactive les boutons
    button1.config(state="normal")
    button2.config(state="normal")
    button3.config(state="normal")
    button4.config(state="normal")
        
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

# Fonction pour réinitialiser la base de données
def reset_database():
    # Désactive tous les boutons
    for button in (button1, button2, button3, button4):
        button.configure(state=tk.DISABLED)

    # Demande confirmation
    confirm = input("Voulez-vous vraiment réinitialiser la base de données ? (Oui/Non) ")
    if confirm.lower() == "oui":
        with open(DB_PATH, "w") as f:
            json.dump({}, f)
        print("La base de données a été réinitialisée !")
    else:
        print("Réinitialisation annulée.")

    # Réactive tous les boutons
    for button in (button1, button2, button3, button4):
        button.configure(state=tk.NORMAL)

# Fonction pour quitter le programme
def quit_program():
    # Désactive tous les boutons
    for button in (button1, button2, button3, button4):
        button.configure(state=tk.DISABLED)

    # Demande confirmation
    confirm = input("Voulez-vous vraiment quitter le programme ? (Oui/Non) ")
    if confirm.lower() == "oui":
        exit()
    else:
        print("Retour au programme.")

    # Réactive tous les boutons
    for button in (button1, button2, button3, button4):
        button.configure(state=tk.NORMAL)

# Crée la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de mots de passe")

# Ajoute la question
question_label = tk.Label(root, text="QUE VOULEZ-VOUS FAIRE ?", font=("Century Gothic", 16, "bold"), pady=20)
question_label.pack()

# Ajoute les boutons
button1 = tk.Button(root, text="Ajouter un nouveau mot de passe", bg="blue", fg="white", font=("Century Gothic", 12), command=add_password)
button1.pack(pady=10)

button2 = tk.Button(root, text="Afficher les mots de passe enregistrés", bg="green", fg="white", font=("Century Gothic", 12), command=view_passwords)
button2.pack(pady=10)

button3 = tk.Button(root, text="Réinitialiser la base de données", bg="red", fg="white", font=("Century Gothic", 12), command=reset_database)
button3.pack(pady=10)

button4 = tk.Button(root, text="Quitter le programme", bg="purple", fg="white", font=("Century Gothic", 12), command=quit_program)
button4.pack(pady=10)

# Lance la boucle principale
root.mainloop()
def chiffrer_message(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            lettre_chiffree = chr((ord(lettre.lower()) - 97 + decalage) % 26 + 97)
            if lettre.isupper():
                lettre_chiffree = lettre_chiffree.upper()
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

message = "Je suis Jules César"
decalage = 3

message_chiffre = chiffrer_message(message, decalage)

print("Message original : ", message)
print("Message chiffré : ", message_chiffre)
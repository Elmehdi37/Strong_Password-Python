print("Pour que votre mot de passe soit fort, vous devez")
print("- Contenir au moins 8 caractères")
print("- Contient au moins une lettre majuscule")
print("- Contenir au moins un chiffre")

def is_strong_password(p):
    length = (len(p) >= 8)
    majuscule = any(i.isupper() for i in p)
    chiffre = any(i.isdigit() for i in p)
    return length and majuscule and chiffre


while True :
    password = input("Entrez un mot de passe ici : ")

    if is_strong_password(password) :
        print("Bravo, vous avez écrit un mot de passe fort")
        break
    else:
        print("Malheureusement, mon mot de passe est faible. Veuillez le retaper")
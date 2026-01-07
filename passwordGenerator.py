import secrets
import string

def gen_password(length):
    allCharacters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(allCharacters) for i in range(length))
    return password

def puissance(password_final):
    score = 0
    if len(password_final) >= 12 : score += 1 
    if any(c.isdigit() for c in password_final) : score += 1
    if any(c.isupper() for c in password_final) : score += 1
    if any(c in string.punctuation for c in password_final) : score += 1

    blocs = score * 5 
    barre = "█" * blocs + "░" * (20 - blocs)
    return barre, score

user_length = input("Entrez la longueur du mot de passe : ")

if user_length.isdigit():
    length = int(user_length)
   
    if length < 8:
        print("La longueur du mot de passe demandée est trop courte.")
    else:
        password_final = gen_password(length)

        ma_barre, mon_score = puissance(password_final)
        print(f"Mot de passe : {password_final}")
        print(f"Sécurité : [{ma_barre}] {mon_score}/4")
else:     
    print("Un nombre est requis !")
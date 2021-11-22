import random

print("*** LE JEU DU NOMBRE MYSTERE ***")
nombre_a_trouver = random.randrange(0,100,5)
i=5

while i> 0:
        print(f"il te reste {i} essai{'s' if i>1 else ''}")

        nombre_utilisateur = input("devine le nombre(un multiple de 5) : ")
        if not nombre_utilisateur.isdigit():
            print("entrez un nombre valide")
            continue

        if int(nombre_utilisateur) < nombre_a_trouver :
            print(f"le nombre mystere est plus grand que {nombre_utilisateur}" )
        elif int(nombre_utilisateur) > nombre_a_trouver :
            print(f"le nombre mystere est plus petit que {nombre_utilisateur}" )
        else :
            break
            
        i -=1
if i==0:
    print(f"Dommage ! le nombre mystere était {nombre_a_trouver} .")
else:
    print(f"Bravo ! le nombre mystere etait bien {nombre_a_trouver} !")
    print(f"Tu as trouvé le nombre en {6- i} essai{'s' if 6-i>1 else ''}")

print("FIN DU JEU")
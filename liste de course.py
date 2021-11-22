import sys 

LISTE = []

MENU = """Choississez parmi les 5 options suivantes

1. Ajouter un élément à la liste de courses

2. Retirer un élément de la liste de courses

3. Afficher les éléments de la liste de courses

4. Vider la liste de courses

5. Quitter le programme
👉 votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("veuillez choisir une option valide...")

    if user_choice == "1":
        item= input("Entrez le nom de l'élément à ajouter à la liste des courses : ")
        LISTE.append(item)
        print(f"l'élément {item} a bien été ajouté à la liste.")

    elif user_choice == "2":
        item = input("Entrez le nom de l'element à retirer de la liste des courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"l'element {item} a bien été retiré de la liste .")
        else:
            print(f"l'element {item} n'est pas dans la liste . ")

    elif user_choice == "3":
        if LISTE:
            print("voici le contenu de votre liste : ")
            for i, element in enumerate(LISTE , 1):
                print(f"{i}. {element}")
        else:
            print("votre liste ne contient aucun element ....")

    elif user_choice == "4":
        LISTE.clear()
        print("la liste a été vidée de son contenu.")

    elif user_choice == "5":
        print("A bientôt")
        sys.exit

    print("_"*50)





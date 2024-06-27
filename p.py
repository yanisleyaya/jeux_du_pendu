import random

def jeu_plus_ou_moins():
    aleatoire = random.randint(1, 10000)
    nombre = int(input("Choisissez un nombre entre 1 et 10000 : "))
    
    while nombre != aleatoire:
        if nombre < aleatoire:
            print("C'est plus")
        elif nombre > aleatoire:
            print("C'est moins")
        
        nombre = int(input("Choisissez un nombre entre 1 et 10000 : "))
    
    print(f"Bravo ! C'était {aleatoire}.")

jeu_plus_ou_moins()


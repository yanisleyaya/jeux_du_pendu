import random

Listedemotsadeviner = [
    'voiture', 'maison', 'chaise', 'table', 'fenetre', 'porte', 'jardin', 'ordinateur',
    'telephone', 'internet', 'television', 'radio', 'journal', 'magasin', 'supermarche',
    'restaurant', 'cafe', 'cinema', 'theatre', 'parc', 'foret', 'plage', 'lac',
    'riviere', 'montagne', 'mer', 'nuage', 'soleil', 'lune', 'etoile', 'pluie',
    'neige', 'vent', 'tempete', 'orage', 'foudre', 'arc-en-ciel', 'printemps', 'ete',
    'automne', 'hiver', 'matin', 'midi', 'soir', 'nuit', 'heure', 'minute', 'seconde',
    'jour', 'semaine', 'mois', 'annee', 'decennie', 'siecle', 'millenaire', 'histoire',
    'geographie', 'mathematiques', 'sciences', 'physique', 'chimie', 'biologie',
    'langue', 'francais', 'anglais', 'espagnol', 'allemand', 'italien', 'russe',
    'chinois', 'arabe', 'japonais', 'indien', 'bresilien', 'canadien', 'americain',
    'europeen', 'asiatique', 'africain', 'oceanien', 'informatique', 'technologie',
    'internet', 'reseau', 'donnees', 'programme', 'logiciel', 'application',
    'site web', 'navigateur', 'serveur', 'email', 'chat', 'forum', 'reseaux sociaux',
    'photo', 'video', 'musique', 'livre', 'journal', 'magazine', 'journaliste',
    'ecrivain', 'auteur', 'lecture', 'ecole', 'college', 'lycee', 'universite',
    'professeur', 'eleve', 'etudiant', 'cours', 'examen', 'note', 'diplome',
    'travail', 'emploi', 'bureau', 'entreprise', 'patron', 'collegue', 'client',
    'projet', 'equipe', 'reunion', 'presentation', 'rapport', 'objectif', 'succes',
    'echec', 'reussite', 'economie', 'finance', 'commerce', 'marche', 'produit',
    'vente', 'achat', 'publicite', 'promotion', 'marketing', 'strategie', 'budget',
    'finance', 'argent', 'banque', 'compte', 'epargne', 'investissement', 'pret',
    'emprunt', 'dette', 'impot', 'taxe', 'administration', 'gouvernement', 'politique',
    'democratie', 'dictature', 'election', 'vote', 'parti', 'opposition', 'parlement',
    'senat', 'assemblee', 'loi', 'justice', 'tribunal', 'juge', 'avocat', 'accuse',
    'crime', 'peine', 'prison', 'sentence', 'proces', 'affaire', 'victime',
    'coupable', 'innocent', 'criminalite', 'violence', 'agression', 'vol', 'vandalisme',
    'droit', 'obligation', 'liberte', 'responsabilite', 'devoir', 'morale', 'ethique',
    'religion', 'croyance', 'spiritualite', 'Dieu', 'foi', 'culte', 'priere',
    'eglise', 'temple', 'mosquee', 'synagogue', 'bouddhisme', 'hindouisme', 'christianisme',
    'islam', 'atheisme', 'agnosticisme', 'philosophie', 'sagesse', 'pensee', 'idee',
    'concept', 'theorie', 'hypothese', 'argument', 'raisonnement', 'logique',
    'raison', 'emotion', 'sentiment', 'amour', 'haine', 'joie', 'tristesse',
    'colere', 'peur', 'bonheur', 'sante', 'maladie', 'medecin', 'infirmier',
    'hopital', 'clinique', 'consultation', 'traitement', 'remede', 'pharmacie',
    'medicament', 'chirurgie', 'operation', 'douleur', 'souffrance', 'sante mentale',
    'psychologie', 'psychiatre', 'therapie', 'psychologue', 'psychotherapie', 'stress',
    'anxiete', 'depression', 'equilibre', 'repos', 'sommeil', 'reve', 'cauchemar',
    'reveil', 'endormissement', 'insomnie', 'sieste', 'repos', 'pause', 'relaxation',
    'meditation', 'zen', 'yoga', 'sport', 'fitness', 'muscle', 'exercice', 'course',
    'natation', 'football', 'basketball', 'volleyball', 'tennis', 'golf', 'rugby',
    'athletisme', 'boxe', 'arts martiaux', 'karate', 'judo', 'taekwondo', 'wushu',
    'equitation', 'cyclisme', 'skateboard', 'surf', 'ski', 'snowboard', 'montagne',
    'escalade', 'randonnee', 'camping', 'voyage', 'aventure', 'exploration',
    'decouverte', 'expedition', 'tourisme', 'vacances', 'destination', 'visite',
    'culture', 'patrimoine', 'tradition', 'coutume', 'folklore', 'art', 'peinture',
    'sculpture', 'musee', 'exposition', 'photographie', 'cinema', 'theatre', 'danse',
    'musique', 'concert', 'spectacle', 'opera', 'ballet', 'orchestre', 'chanson',
    'instrument', 'guitare', 'piano', 'violon', 'flute', 'trompette', 'batterie',
    'chant', 'voix', 'chorale', 'symphonie', 'comedie', 'drame', 'fiction', 'poesie',
    'romance', 'thriller', 'action', 'aventure', 'fantasy', 'science-fiction',
    'horreur', 'western', 'histoire', 'biographie', 'autobiographie', 'essai', 'critique',
    'lecture', 'bibliotheque', 'librairie', 'livre', 'auteur', 'ecrivain', 'lecture',
    'education', 'apprentissage', 'connaissance', 'savoir', 'sagesse', 'culture',
    'science', 'mathematiques', 'physique', 'chimie', 'biologie', 'geographie',
    'histoire', 'langue', 'francais', 'anglais', 'espagnol', 'allemand', 'russe',
    'chinois', 'arabe', 'japonais', 'coreen', 'portugais', 'italien', 'neerlandais',
    'suedois', 'norvegien', 'danois', 'finlandais', 'hebreu', 'hindi', 'turc',
    'grec', 'polonais', 'tcheque', 'slovaque', 'hongrois', 'roumain', 'bulgare',
    'serbe', 'croate', 'ukrainien', 'lituanien', 'letton', 'estonien', 'islandais',
    'gallois', 'ecossais', 'irlandais', 'americain', 'canadien', 'mexicain', 'bresilien',
    'argentin', 'chilien', 'colombien', 'peruvien', 'venezuelien', 'equatorien',
    'bolivien', 'paraguayen', 'uruguayen', 'costaricien', 'salvadorien', 'guatemalteque',
    'panameen', 'hondurien', 'nicaraguayen', 'cubain', 'dominicain', 'haitien', 'portoricain',
    'jamaicain', 'bahameen', 'belizien'
]

def choisir_mot():
    return random.choice(Listedemotsadeviner) # choisie un mot aléatoire

def jeu_du_pendu():
    mot_a_deviner = choisir_mot()
    taille_mot = len(mot_a_deviner)
    mot_en_cours = ['-'] * taille_mot # transforme le mot_a_deviner ['-']
    compteur = 0 # mais compteur a 0
    erreur =  0 # mais erreur a 0
    while ''.join(mot_en_cours) != mot_a_deviner:
        print(mot_a_deviner)  
        print("Mot à deviner :", ' '.join(mot_en_cours)) 
        entree = input("Entrez un mot : ") # entré est = a se que l'on ecrit
        
        for i in range(min(len(entree), len(mot_a_deviner))):
            if entree[i] == mot_a_deviner[i]:
                mot_en_cours[i] = entree[i] 
        
        compteur += 1 

        if ''.join(mot_en_cours) == mot_a_deviner: # dit sie tu a reussi 
            print("Félicitations ! Vous avez deviné le mot :", mot_a_deviner)
            break

        if entree != mot_a_deviner: # rajoute une partie du pendu par erreur 
            erreur = erreur + 1
            if erreur >= 1:
                print(" ||/       |  ")
            if erreur >= 2:
                print(" ||        0  ")
            if erreur >= 3:
                print(" ||       /|\ ")
            if erreur >= 4:
                print(" ||       /|  ")
            if erreur >= 5:
                print("/||           ")
            if erreur >= 6: 
                print("==============")
                print("Désolé, vous avez perdu. Le mot était :", mot_a_deviner)
                break # mais fin au programe si on fait 6 erreurs
jeu_du_pendu()
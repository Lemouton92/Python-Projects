# -*-coding:utf-8 -*

import os
from random import randrange
from math import ceil
#Déclaration des variables
argent=1000
continuer_partie=True
mise_jeu1 = 0
Score=0

print("Bienvenue au Casino !")
Jeu=input("A quel jeu voulez vous jouer ? Le Nombre Aléatoire (0) ou La Roulette (1) ? : ")
#Erreurs
try:
    Jeu = int(Jeu)
except ValueError:
    print("Vous n'avez pas saisi de nombre")
    Jeu = -1
    continue
if Jeu < 0:
    print("Ce nombre est négatif")
if Jeu > 1:
    print("Ce nombre est supérieur à 1")
#Tant que la variable boléenne continuer_partie est vraie, la partie continue
while continuer_partie:

	if Jeu==0:
	    print("Vous avez sélectionné le jeu du Nombre Aléatoire.")
	    mise_jeu0 = 0
	    while mise_jeu0 <= 0 or mise_jeu0 > argent:
	        mise_jeu0 = input("Tapez le montant de votre mise : ")
	        # On convertit la mise
	        try:
	            mise_jeu0 = int(mise)
	        except ValueError:
	            print("Vous n'avez pas saisi de nombre")
	            mise_jeu0 = -1
	            continue
	        if mise_jeu0 <= 0:
	            print("La mise saisie est négative ou nulle.")
	        if mise_jeu0 > argent:
	            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")
	    NombreRandom=randrange(1,100)
		
	    NombreJoueur=input("Merci d'entrer un nombre compris entre 1 et 100 :  ")
		
		while NombreJoueur != NombreRandom:
			if NombreJoueur < NombreRandom:
				NombreJoueur=input("Plus : ")
				Score += 1
			elif NombreJoueur > NombreRandom:
				NombreJoueur=input("Moins : ")
				Score += 1

		if Score==0:
			mise_jeu0*=10
			print("Bravo, vous avez trouvé du premier coup ! Vous obtenez", mise_jeu0)
			argent += mise_jeu0
		elif Score==1:
			mise_jeu0*6
			print("Vous avez trouvé avec 2 essais seulement ! Vous obtenez", mise_jeu0)
			argent += mise_jeu0
		elif Score==2:
			mise_jeu0*=3
			print("Vous avez trouvé en 3 essais ! Vous obtenez", mise_jeu0)
			argent += mise_jeu0
		elif Score==3:
			mise_jeu0*=2
			print("Vous avez trouvé en 4 essais ! Vous obtenez", mise_jeu0)
			argent += mise_jeu0
		elif Score==4:
			print("Vous avez trouvé en 5 essais ! Vous obtenez", mise_jeu0)
			argent += mise_jeu0
		elif Score==5:
		 	print("Vous avez trouvé en 6 essais ! Vous ne perdez pas votre mise")
		elif Score > 5:
			Score += 1
			print("Vous avez trouvé en ", Score,"essais ! Malheureusement vous perdez votre mise")
			# On interrompt la partie si le joueur est ruiné
	    if argent <= 0:
	        print("Vous êtes ruiné ! C'est la fin de la partie.")
	        continuer_partie = False
	    else:
	        # On affiche l'argent du joueur
	        print("Vous avez à présent", argent, "$")
	        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
	        if quitter == "o" or quitter == "O":
	            print("Vous quittez le casino avec vos gains.")
	            continuer_partie = False
	        Jeu = input("Souhaiter-vous changez de jeu ?")
	
	elif Jeu==1:
		print("Vous avez sélectionné le jeu de la Roulette")
		nombre_roulette = -1
		while nombre_roulette < 0 or nombre_roulette > 49:
		    nombre_roulette = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
		    # On convertit le nombre misé
		    try:
		        nombre_roulette = int(nombre_mise)
		    except ValueError:
		        print("Vous n'avez pas saisi de nombre")
		        nombre_roulette = -1
		        continue
		    if nombre_roulette < 0:
		        print("Ce nombre est négatif")
		    if nombre_roulette > 49:
		        print("Ce nombre est supérieur à 49")		

	    # À présent, on sélectionne la somme à miser sur le nombre
	    
	    while mise_jeu1 <= 0 or mise_jeu1 > argent:
	        mise_jeu1 = input("Tapez le montant de votre mise : ")
	        # On convertit la mise
	        try:
	            mise_jeu1 = int(mise)
	        except ValueError:
	            print("Vous n'avez pas saisi de nombre")
	            mise_jeu1 = -1
	            continue
	        if mise_jeu1 <= 0:
	            print("La mise saisie est négative ou nulle.")
	        if mise_jeu1 > argent:
	            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

	    # Le nombre misé et la mise ont été sélectionnés par
	    # l'utilisateur, on fait tourner la roulette
	    numero_gagnant = randrange(50)
	    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

	    # On établit le gain du joueur
	    if numero_gagnant == nombre_mise:
	        print("Félicitations ! Vous obtenez", mise * 3, "$ !")
	        argent += mise * 3
	    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
	        mise = ceil(mise * 0.5)
	        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
	        argent += mise
	    else:
	        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
	        argent -= mise

        if argent <= 0:
	        print("Vous êtes ruiné ! C'est la fin de la partie.")
	        continuer_partie = False
	    else:
	        # On affiche l'argent du joueur
	        print("Vous avez à présent", argent, "$")
	        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
	        if quitter == "o" or quitter == "O":
	            print("Vous quittez le casino avec vos gains.")
	            continuer_partie = False
	        Jeu = input("Souhaiter-vous changez de jeu ?")


















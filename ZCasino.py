# -*-coding:utf-8 -*

from random import randrange
from math import ceil
#On demande au joueur une somme à miser
Pari = input("Choisissez une somme à miser située entre 2 et 1000")
#Script Erreurs
try:
	Pari = int(Pari)
	assert Pari >= 2 and Pari <= 1000
except ValueError:
	print("Vous n'avez pas saisi un nombre entier")
except AssertionError:
    print("La somme n'est pas comprise entre 2 et 1000")
else:
	print("Vous avez parié",Pari,"$")     
#On demande au joueur un nombre entre 0 et 49
NombreJoueur = input("Choisissez un nombre situé entre 0 et 49")
#Script Erreurs
try:
	NombreJoueur = int(NombreJoueur)
	assert NombreJoueur >= 0  and NombreJoueur <= 49
except ValueError:
	print("Vous n'avez pas saisi un nombre entier")
except AssertionError:
    print("Le nombre choisi n'est pas compris entre 0 et 50")
else:
	print("Vous avez choisi le nombre",NombreJoueur,)
#On determine la couleur de NombreJoueur en fonction de si il est pair ou impair
if NombreJoueur % 2 == 0:
	print("Votre nombre est pair, il est donc de couleur Noire")
	CouleurJoueur = 0
else:
    print("Votre nombre est impair, il est donc de couleur Rouge")
    CouleurJoueur = 1
#On créé un Nombre Aléatoire entre 0 et 49
NombreAleatoire = randrange(50)
#On determine la couleur de NombreAleatoire
if NombreAleatoire % 2 == 0:
	print("Le Nombre Aléatoire est",NombreAleatoire,", il est pair et donc de couleur Noire")
	CouleurAleatoire = 0
else:
    print("Le Nombre Aléatoire est",NombreAleatoire,", il est impair et donc de couleur Rouge")
    CouleurAleatoire = 1
#On determine si le joueur a gagné ou pas
if NombreAleatoire == NombreJoueur:
	Pari = Pari * 3
	print("Bravo vous avez gagné",Pari,"$  !!!")
elif CouleurAleatoire == CouleurJoueur:
    Pari = Pari / 2
    Pari = ceil(Pari)
    print("Vous n'avez pas gagné, mais les deux nombres sont de la même couleur, on vous rend donc",Pari,"$")
else:
    print("Vous avez perdu !!!")              






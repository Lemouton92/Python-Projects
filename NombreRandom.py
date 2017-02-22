# -*-coding:utf-8 -*

from random import randrange

NombreJoueur=input("Merci d'entrer un nombre compris entre 1 et 100 :  ")

NombreRandom=randrange(1,100)

while NombreJoueur != NombreRandom:
	if NombreJoueur < NombreRandom:
		NombreJoueur=input("Plus : ")
	elif NombreJoueur > NombreRandom:
		NombreJoueur=input("Moins : ")

if NombreJoueur==NombreRandom:
	print("Bravo vous avez trouvé !!!")	
	
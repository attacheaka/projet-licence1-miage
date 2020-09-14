# Importation des functions
from functions import Classe
from functions import Etudiant
from functions import Note

# Description du menu en dictionnaire
menu = {
	"0" : "Crée une classe",
	"1" : "Inscription d'un etudiant",
	"2" : "Saisir les notes",
	"3" : "Afficher les notes",
	"4" : "Afficher la moyenne",
	"5" : "pour quitter le programme"
}

# Affichage du dictatiel 
print("Programme de gestion d'inscription scolaire")
print("Menu du programme tapez : \n")

# Fonction pour afficher le menu
def choix():
	for optionChoisi in menu:
		print("{} - {}".format(optionChoisi,menu[optionChoisi]))

# Fonction demarrer les fonctionnalités du programme en fonction du choix de l'utilisateur
# Parametre de la fonction x 
def actions(x):
	if x == "0":
		Classe.create()
	elif x == "1":
		Etudiant.create()
	elif x == "2":
		Note.create()
	elif x == "3":
		Note.read()
	elif x == "4":
		Note.moyenne()
	elif x == "5":
		print("Aurevoir !!!")
		exit()

# Appels à la fonction choix
choix()

# Lance une saisi à l'ecran de l'utilisateur
x = input("\nEntrez votre choix : \n")

# Appel de la fonction action
actions(x)

# Boucle qui controle la saisie de l'utilisateur en cas de valeur incorrect lié aux options du menu
while not x in menu.keys():
	print("\n!!! Oups option invalid veuillez ressayer \n")
	choix()
	x = input("\nEntrez votre choix : \n")
	actions(x)
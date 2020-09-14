# Fonction pour créer une classe
def create():
	data = []
	code = input("Entrez le code de la classe : ")
	libelle = input("Entrez le libelle de la classe : ")
	data = "Code = {}\nLibelle = {}\n\n".format(code,libelle)
	with open('database/classe.txt',"a") as file:
		file.write(data)

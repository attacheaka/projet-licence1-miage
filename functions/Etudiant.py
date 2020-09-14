# Fonction pour inscrire un étudiant
def create():
	nom = input("Entrez le nom de l'etudiant : ")
	prenom = input("Entrez le prenom de l'etudiant : ")
	matricule = input("Entrez le matricule de l'etudiant")
	data = "Nom = {}\nPrenom = {}\nMatricule = {}\n\n".format(nom,prenom,matricule)
	with open('datas/etudiant.txt',"a") as file:
		file.write(data)

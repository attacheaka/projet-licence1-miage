# Fonction pour afficher les notes
def read():
	values = []
	with open('datas/note.txt','r') as file:
		print("Liste des notes\n")
		print(file.read())

# Fonction pour saisir les notes
def create():
	note = input("Entrez la note : ")
	data = "{}\n".format(note)
	with open('datas/note.txt',"a") as file:
		file.write(data)

# Fonction pour calculer la moyenne des notes
def moyenne():
	notes = []
	somme = 0
	with open('datas/note.txt','r') as file:
		notes = file.read().split("\n")
		for note in notes:
			somme += int(note)
		moyenne = somme / len(notes)
		print(round(moyenne,2))
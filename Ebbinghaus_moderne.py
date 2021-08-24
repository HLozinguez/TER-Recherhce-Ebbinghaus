'''Convention de nommage par apparition dans le code:

us_syl= used syllabes (pour les syllabes qui ont déjà été sélectionnées dans une liste)
cr_list= created lists (pour les listes de syllabes qui ont déjà été créées)
cmpl_syl= complete syllables (pour la liste de l'ensemble des syllabes possibles)
t= taille (pour le nombre de syllabes de la liste)
n= nombre (pour le nombre de listes initiales voulues)
'''

from random import randint
from os import path

us_syl=[]
#used syllables: Permet de retenir les syllabes déjà utilisées pour la création d'une liste.
cr_list=[]
#created lists: Permet de retenir les listes de syllabes qui ont déjà été crées.
d_lists=[]
#derived lists: Permet de retenir les listes dérivées qui ont déjà été formées.

def creasyl ():
	'''returns all accepted syllables'''
	v=["a","eu","i","o","u","é","ou","aï","un","en"]
	#Liste des voyelles utilisées pour créer les syllabes.
	c=["b","s","d","f","g","ch","j","k","l","m","n","p","r","t","v","x","z"]
	#Liste des consonnes utilisées pour créer les syllabes.
	cmpl_syl=[]
	#Initialisation de la liste de toutes les syllabes.
	for i in c:
		#Parcours des consonnes et des syllabes pour créer toutes les syllabes possibles.
		for j in v:
			for k in c:
				if i !=k:
					#Non prise en compte des syllabes dont la consonne de départ et d'arrivée est la même.
					cmpl_syl.append(i+j+k)

	cmpl_syl_save=open("cmpl_syl.txt","w")
	#Creation d'un document de sauvegarde des syllabes.
	cmpl_syl_save.write("Voici la liste complète des syllabes crées par le programme:\nsyl=[")
	#Enregistement des syllabes dans le document cmpl_syl.txt.
	for i in range(len(cmpl_syl)):
		if i!=len(cmpl_syl)-1:
			cmpl_syl_save.writelines("{},".format(cmpl_syl[i]))
		else:
			cmpl_syl_save.writelines("{}]".format(cmpl_syl[i]))
	return cmpl_syl
	#Renvoi de la liste des syllabes pour la suite du programme.


def crealist (t=12,s=creasyl()):
	'''retourne une liste de syllabes'''
	list_syl=[]
	#Initilisation d'une liste de syllabes.
	while len(list_syl)<t:
		#Tant que la liste ne contient pas autant de syllabes que souhaité.
		syl=s[randint(0,len(s)-1)]
		#Choix d'une syllabe au hasard parmi les syllabes créees.
		global us_syl
		#Permet de modifier la variable globale us_syl du programme.
		if syl not in us_syl:
			#Verification de l'absence de la syllabe selectionnée de la liste des syllabes déjà utilisées us_syl.
			us_syl.append(syl)
			#Dans ce cas, ajout de la syllabe à la liste des syllabes utilisées us_syl.
			list_syl.append(syl)
			#Puis ajout de la syllabe à la liste de syllabes en cours de création.

	list_syl_save=open("list_syl.txt","a")
	if path.getsize("list_syl.txt")==0:
		list_syl_save.write("Voici la liste des listes de syllabes qui ont déjà été crées:\n[")
	list_syl_save.write("[")
	for i in range (len (list_syl)):
		if i!=len(list_syl)-1:
			list_syl_save.writelines("{},".format(list_syl[i]))
		else:
			list_syl_save.writelines("{}]".format(list_syl[i]))
	return list_syl
	#Renvoi de la liste de syllabes pour la suite du programme.


def up_list (t=12,s=creasyl()):
	'''Crée une liste de syllabes puis mets à jour
	la liste des syllabes créées et la retourne.'''
	l=crealist(t,s)
	#Creation de la liste de syllabe
	global cr_list
	cr_list.append(l)
	#Mise à jours
	return cr_list
	#Renvoi la liste de syllabes créees


def all_lists(n=6,t=12,s=creasyl()):
	'''Crée le nombre de listes de notre choix, avec le nombre de syllabes
	de notre choix, par défaut 6 listes de 12 syllabes, puis retourne toutes les listes'''
	for i in range (n):
		#Crée le nombre de liste n de notre choix
		up_list(t,s)
	list_syl_save=open("list_syl.txt","a")
	list_syl_save.write("]")
	return cr_list
	#Renvoi toutes les listes



def derivee_sub_lists(o=2,liste=cr_list):
	'''Crée les listes dérivées d'ordre o à partir de toutes les listes
	crées dans cr_list, en utilisant des sous listes.'''
	d=[]
	#Initilisation d'une liste
	for i in liste:
		valeur=0
		inter=[]
		for j in range (o+1):
			inter.append([])
			for k in i:
				if valeur%(o+1)==j:
					inter[j].append(k)
				valeur+=1
				#Crée les dérivés
		d.append(inter)
	return(d)
	#Renvoi les listes

def derivee_complete(o=2,liste=cr_list):
	'''Crée les listes dérivées d'ordre o à partir de toutes les listes
	crées dans cr_list, sans utiliser de sous listes.'''
	d=[[] for i in range(len(liste))]
	#Initialisation
	count=0
	#Initialisation d'une varibale
	for i in liste:
		valeur=0
		for j in range (o+1):
			for k in i:
				if valeur%(o+1)==j:
					d[count].append(k)
				valeur+=1
				#Crée les dérivés
		count+=1
	return(d)
	#Renvoi toutes les listes de dérivés

def all_derivees(listes=all_lists(n=2)):
	'''Fais toutes les dérivées et les mets dans un fichier .txt'''
	d_list = [[]for i in range(len(listes))]
	#Initialisation
	taille = len(listes[0])
	f=open("derivee.txt","w")
	#Definition du fichier txt
	for i in range(len(listes)):
		count=1
		while count!=taille:
			if taille % count==0:
				d=(derivee_complete(count-1))
				#Utilise la fonction définies plus tôt pour faire les dérivées
				d_list[i].append(d[i])
				f.writelines("liste derivée de la liste {} d'ordre {} : {} \n".format(i+1,count-1,d[i]))
			count+=1
	return d_list

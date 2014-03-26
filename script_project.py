from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient 
import re

#les 5 dernieres saisons du championnat ligue 1 francaise
saisons =["2012-2013","2011-2012","2010-2011","2009-2010" ] 
#les liens des sources
source_e = "http://sport24.lefigaro.fr/livescore/football/ligue-1/SA/38eme-journee/classement?tableau=exterieur"
source_d = "http://sport24.lefigaro.fr/livescore/football/ligue-1/SA/38eme-journee/classement?tableau=domicile"
source = "http://sport24.lefigaro.fr/livescore/football/ligue-1/SA/38eme-journee/classement?tableau=general"

####
##cette fonction return la liste des d equipes  
####
def get_club(tag):
	return  tag == "tabPiloteBleuPil " or  tag == "tabPiloteBlancPil " 

####
##cette fonction return le classement de l equipe pendant les 5 dernier annees 
####
def get_classement(equipe):
	li = []
	for s in saisons : 
		new_source = source.replace("SA",str(s) )
		new_source1 = source_e.replace("SA",str(s) )
		new_source2 = source_d.replace("SA",str(s) )
		statis = []
		htmlSource =   urllib.urlopen(new_source).read()
		soup = BeautifulSoup(htmlSource,"lxml")
		for item in soup.find_all(class_="tabPiloteBleuPil ") :
			if (item.find('a').string == equipe ) :
				stat = {}
				stat["saison"] = s 
				stat["classement"] = item.find('span').string 
				for item in [new_source1,new_source2] : 
					htmlS =   urllib.urlopen(item).read()
					sou = BeautifulSoup(htmlS,"lxml")
					for item1 in sou.find_all(class_="tabPiloteBleuPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil lignePointClassement") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
				li.append(stat)
		#li.append(statis)
		for item in soup.find_all(class_="tabPiloteBlancPil ") :
			if (item.find('a').string == equipe ) :
				stat = {}
				stat["saison"] = s 
				stat["classement"] = item.find('span').string 
				for item in [new_source1,new_source2] : 
					htmlS =   urllib.urlopen(item).read()
					sou = BeautifulSoup(htmlS,"lxml")
					for item1 in sou.find_all(class_="tabPiloteBleuPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil lignePointClassement") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
				li.append(stat)
		#li.append(statis)
		for item in soup.find_all(class_="tabPiloteBlancPil lignePointClassement") :
			if (item.find('a').string == equipe ) :
				stat = {}
				stat["saison"] = s 
				stat["classement"] = item.find('span').string 
				for item in [new_source1,new_source2] : 
					htmlS =   urllib.urlopen(item).read()
					sou = BeautifulSoup(htmlS,"lxml")
					for item1 in sou.find_all(class_="tabPiloteBleuPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil ") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
					for item1 in sou.find_all(class_="tabPiloteBlancPil lignePointClassement") : 
						if (item1.find('a').string == equipe ) :
							index = 0 
							for ele in item1.find_all('p') :
								if (index == 2 and item == new_source1) : 
									stat["ge"] = ele.string
									break
								if (index == 2 and item == new_source2) : 
									stat["gd"] = ele.string
									break
								index+=1
				li.append(stat)
		#li.append(statis)
	return li  
		#print soup.find_all(href=re.compile("elsie"))
		


####
##connection avec la base mongodb
####
try:
    conn=MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
db = conn.local
eqiupes_collection = db.equipes

#recuperation de donnees.
#for s in saisons : 
#	print s 
	#new_source = source.replace("SA",str(s) )
htmlSource =   urllib.urlopen("http://sport24.lefigaro.fr/livescore/football/ligue-1/2013-2014/1ere-journee/classement?tableau=general").read()
soup = BeautifulSoup(htmlSource,"lxml")
equipes = []
code = 0
for item in soup.find_all(class_="tabPiloteBleuPil ") : 
	code+=1
	equipe = {}
	equipe["nom"] =  item.find('a').string
	equipe["code_equipe"] = code
	equipe["stat"] = get_classement(item.find('a').string)
	equipes.append(equipe)
for item in soup.find_all(class_="tabPiloteBlancPil ") :
	code+=1
	equipe = {}
	equipe["nom"] =  item.find('a').string
	equipe["code_equipe"] = code
	equipe["stat"] = get_classement(item.find('a').string)
	equipes.append(equipe)
for item in soup.find_all(class_="tabPiloteBlancPil lignePointClassement") :
	code+=1
	equipe = {}
	equipe["nom"] =  item.find('a').string
	equipe["code_equipe"] = code
	equipe["stat"] = get_classement(item.find('a').string)
	equipes.append(equipe)
	
print equipes
eqiupes_collection.insert(equipes)


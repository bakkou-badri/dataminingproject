from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient 
import re
import numpy as np

jours = ["1ere-journee" ,"2eme-journee" ,"3eme-journee" ,"4eme-journee" ,"5eme-journee" ,"6eme-journee" ,"7eme-journee" ,"8eme-journee" ,
		"9eme-journee" ,"10eme-journee" ,"11eme-journee" ,"12eme-journee" ,"13eme-journee" ,"14eme-journee" ,"15eme-journee" ,"16eme-journee" ,
		"17eme-journee" ,"18eme-journee" ,"19eme-journee" ,"20eme-journee" ,"21eme-journee" ,"22eme-journee" ,"23eme-journee" ,"24eme-journee" ,
		"25eme-journee" ,"26eme-journee" ,"27eme-journee" ,"28eme-journee" ,"29eme-journee" ,"30eme-journee" ,"31eme-journee" ,"32eme-journee" ,
		"33eme-journee" ,"34eme-journee" ,"35eme-journee" ,"36eme-journee" ,"37eme-journee" ,"38eme-journee"]

codage_equipes = []
moyenne_equipes_ge = []
moyenne_equipes_gd = []

"""
cette fonction return la code de l equipe
"""
def get_equipe_code(equipe):
	for item  in codage_equipes :
		if (equipe == item.values()[0] ) :
			return item.keys()[0] 

#connection a la base de donnee
try:
    conn=MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
db = conn.local
equipes = db.equipes
resultats = db.resultats



for item in equipes.find():
	#for key in item :
		#print key, ' valaue is ', item[key]
	equipe = {}
	moy_ge = {}
	moy_gd = {}
	equipe[item['code_equipe']] = item['nom']
	#print item['nom'], 'stat is ',  item['stat']
	moyenne_ge = 0
	moyenne_gd = 0  
	for ele in item['stat'] : 
		print ele['saison'] , ' moyen ganer ', ele['ge']/18 
		moyenne_ge += int(ele['ge']) 
		moyenne_gd += int(ele['gd'])
	moy_ge[item['code_equipe']] = moyenne_ge
	moy_gd[item['code_equipe']] = moyenne_gd
	codage_equipes.append(equipe)
	moyenne_equipes_ge.append(moy_ge)
	moyenne_equipes_gd.append(moy_gd)

print codage_equipes
print moyenne_equipes_ge
print moyenne_equipes_gd

a=np.eye(len(codage_equipes),len(codage_equipes))
print a 
print resultats.count()
for item in  resultats.find():
	for key in  item :
		if key in jours : 
			for ele in  item[key] :
				eq1_res =  int(ele['res'].split('-')[0] )
				eq2_res =  int(ele['res'].split('-')[1] )
				c = get_equipe_code(ele['eq1']) 
				l = get_equipe_code(ele['eq2'])
				if (c != None and l != None) : 
					#print a.item((int(c)-1, int(l)-1))
					print c , ' VS ' , l
					print eq1_res , ' - ' , eq2_res
					if ( eq1_res > eq2_res) : 
						a[int(c)-1,int(l)-1] = a[int(c)-1,int(l)-1] + 1
					
list1 = [2,5,13,6,8,12,11,10,15]
list2 = [3,18,14,5,9,16,1,4,17]



print a 			











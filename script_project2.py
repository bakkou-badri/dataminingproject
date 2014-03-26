from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient 
import re


saisons = ["2012-2013","2011-2012","2010-2011"] 
jours = ["1ere-journee" ,"2eme-journee" ,"3eme-journee" ,"4eme-journee" ,"5eme-journee" ,"6eme-journee" ,"7eme-journee" ,"8eme-journee" ,
		"9eme-journee" ,"10eme-journee" ,"11eme-journee" ,"12eme-journee" ,"13eme-journee" ,"14eme-journee" ,"15eme-journee" ,"16eme-journee" ,
		"17eme-journee" ,"18eme-journee" ,"19eme-journee" ,"20eme-journee" ,"21eme-journee" ,"22eme-journee" ,"23eme-journee" ,"24eme-journee" ,
		"25eme-journee" ,"26eme-journee" ,"27eme-journee" ,"28eme-journee" ,"29eme-journee" ,"30eme-journee" ,"31eme-journee" ,"32eme-journee" ,
		"33eme-journee" ,"34eme-journee" ,"35eme-journee" ,"36eme-journee" ,"37eme-journee" ,"38eme-journee"]

source = "http://sport24.lefigaro.fr/livescore/football/ligue-1/SA/J"


####
##connection avec la base mongodb
####
try:
    conn=MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e 
db = conn.local
resultats_collection = db.resultats

r = []
resultats = []

for s in saisons : 
	new_source = source.replace("SA",str(s) )
	dic = {}
	dic["saisons"] = s
	for j in jours : 
		lis = []
		new_source1 = new_source.replace("J",str(j) )
		htmlSource =   urllib.urlopen(new_source1).read()
		soup = BeautifulSoup(htmlSource,"lxml")
		#match_class a tester soup.findAll(match_class("feeditemcontent cxfeeditemcontent"))
		for item in soup.find_all(class_="fdBlancheGhe") : 
			res = {}
			index  = 0
			for ele in item.find_all('a'):
				if (index == 0 ) :
					res["eq1"] = ele.string 
				if (index == 1 and ele['class'] == "scoreAgenda") :
					res["res"] = ele.string#test si n est pas un lien if n.name == 'p' and n['class'] == "poem": 
				else:
					for d in item.find_all(class_="scoreAgenda") :
						res["res"] = d.string
				if (index == 2 ) :
					res["eq2"] = ele.string 
				index += 1
			lis.append(res)
		for item in soup.find_all(class_="fdBleueClairGhe") : 
			res = {}
			index = 0
			for ele in item.find_all('a'):
				if (index == 0 ) :
					res["eq1"] = ele.string 
				if (index == 1 and ele['class'] == "scoreAgenda") :
					res["res"] = ele.string#test si n est pas un lien if n.name == 'p' and n['class'] == "poem": 
				else:
					for d in item.find_all(class_="scoreAgenda") :
						res["res"] = d.string
				if (index == 2 ) :
					res["eq2"] = ele.string 
				index += 1 
			lis.append(res)
		dic[j] = lis
		#print 'saison', s, ' jours ', j
		#print lis
	resultats.append(dic)
print resultats
resultats_collection.insert(resultats)



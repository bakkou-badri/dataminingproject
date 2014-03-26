from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient 
import re
import numpy as np

##declaration des listes 
jours = ["1ere-journee" ,"2eme-journee" ,"3eme-journee" ,"4eme-journee" ,"5eme-journee" ,"6eme-journee" ,"7eme-journee" ,"8eme-journee" ,
		"9eme-journee" ,"10eme-journee" ,"11eme-journee" ,"12eme-journee" ,"13eme-journee" ,"14eme-journee" ,"15eme-journee" ,"16eme-journee" ,
		"17eme-journee" ,"18eme-journee" ,"19eme-journee" ,"20eme-journee" ,"21eme-journee" ,"22eme-journee" ,"23eme-journee" ,"24eme-journee" ,
		"25eme-journee" ,"26eme-journee" ,"27eme-journee" ,"28eme-journee" ,"29eme-journee" ,"30eme-journee" ,"31eme-journee" ,"32eme-journee" ,
		"33eme-journee" ,"34eme-journee" ,"35eme-journee" ,"36eme-journee" ,"37eme-journee" ,"38eme-journee"]

codage_equipes = []
moyenne_equipes_ge = []
moyenne_equipes_gd = []

def get_mongodb_connection():
	#connection a la base de donnee
	try:
		conn=MongoClient()
		print "Connected successfully!!!"
	except pymongo.errors.ConnectionFailure, e:
		print "Could not connect to MongoDB: %s" % e 
	db = conn.local
	equipes = db.equipes
	resultats = db.resultats
	return (equipes,resultats)

"""
cette fonction return la code de l equipe
"""
def get_equipe_code(equipe):
	for item  in codage_equipes :
		if (equipe == item.values()[0] ) :
			return item.keys()[0] 


def init_param_algo(): 
	print 'start init '
	equipes , resultats = get_mongodb_connection()
	for item in equipes.find():
		equipe = {}
		moy_ge = {}
		moy_gd = {}
		equipe[item['code_equipe']] = item['nom']
		moyenne_ge = 0
		moyenne_gd = 0  
		for ele in item['stat'] : 
			moyenne_ge += int(ele['ge']) 
			moyenne_gd += int(ele['gd'])
		moy_ge[item['code_equipe']] = moyenne_ge
		moy_gd[item['code_equipe']] = moyenne_gd
		codage_equipes.append(equipe)
		moyenne_equipes_ge.append(moy_ge)
		moyenne_equipes_gd.append(moy_gd)
	a=np.eye(len(codage_equipes),len(codage_equipes))
	for item in  resultats.find():
		for key in  item : 
			if key in jours :  
				for ele in  item[key] : 
					eq1_res =  int(ele['res'].split('-')[0] )
					eq2_res =  int(ele['res'].split('-')[1] )
					c = get_equipe_code(ele['eq1']) 
					l = get_equipe_code(ele['eq2'])
					if (c != None and l != None) : 
						if ( eq1_res > eq2_res) : 
							a[int(c)-1,int(l)-1] = a[int(c)-1,int(l)-1] + 1
	print 'end of init'
def prediction_algo(val1,val2):
	print 'start algo'
	print 'end algo'

def get_prediction(val1,val2):
	print 'call function '
	init_param_algo()
	prediction_algo(val1,val2)







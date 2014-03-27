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
matrice_pro = None

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

def get_moye_vict_domicile(code_equipe):
	som = .0
	flag = 0.8
	nb=0
	for item  in moyenne_equipes_gd :
		for ele in item : 
			if (ele == code_equipe):
				for elem in item[ele] : 
					som = som +  elem*flag
					flag -=0.2
					nb+=1
			else :
				return .0
	return  som/nb

def matrice_moy_match(a,b):
	print 'call function matrice myen'
	for i in range(len(codage_equipes)) :
		print i
		for j in range(len(codage_equipes)) :
			print j
			if  (b[i,j] != 0 ) :
				matrice_pro[i,j] = a[i,j]/b[i,j]


def get_similarite(a,index):
	return a[index,3]

def init_param_algo(): 
	print 'start init '
	equipes , resultats = get_mongodb_connection()
	for item in equipes.find():
		equipe = {}
		moy_ge = {}
		moy_gd = {}
		equipe[item['code_equipe']] = item['nom']
		moyenne_ge = []
		moyenne_gd = []   
		for ele in item['stat'] : 
			moyenne_ge.append(float(ele['ge'])/18) 
			moyenne_gd.append(float(ele['gd'])/18)
		moy_ge[item['code_equipe']] = moyenne_ge
		moy_gd[item['code_equipe']] = moyenne_gd
		codage_equipes.append(equipe)
		moyenne_equipes_ge.append(moy_ge)
		moyenne_equipes_gd.append(moy_gd)
	a=np.eye(len(codage_equipes),len(codage_equipes))
	b=np.eye(len(codage_equipes),len(codage_equipes))
	M=np.eye(len(codage_equipes),len(codage_equipes))
	matrice_pro=np.eye(len(codage_equipes),len(codage_equipes))
	for item in  resultats.find():
		for key in  item : 
			if key in jours :  
				for ele in  item[key] : 
					eq1_res =  int(ele['res'].split('-')[0] )
					eq2_res =  int(ele['res'].split('-')[1] )
					c = get_equipe_code(ele['eq1']) 
					l = get_equipe_code(ele['eq2'])
					if (c != None and l != None) : 
						b[int(c)-1,int(l)-1] = b[int(c)-1,int(l)-1] + 1
						M[int(c)-1,int(l)-1] = float(0)
						if ( eq1_res > eq2_res) : 	
							a[int(c)-1,int(l)-1] = a[int(c)-1,int(l)-1] + 1
	for i in range(len(codage_equipes)) :
		for j in range(len(codage_equipes)) :
			if  (b[i,j] != 0 ) :
				M[i,j] = a[i,j]/b[i,j]
	print 'end of init'
	return M

def prediction_algo(M,val1,val2):
	print 'start algo'
	print val1
	print val2
	resu= []
	for item in range(len(val1)):
		dic = {}
		eq1 =  get_equipe_code(val1[item]['nom']) 
		eq2 = get_equipe_code(val2[item]['nom'])
		print 'code eq1 ' , eq1 , 'code eq2 ', eq2
		print M[int(eq1)-1,int(eq2)-1], ' prop de ganger ' , M[int(eq1)-1,int(eq2)-1]*0.6
		print get_moye_vict_domicile(int(eq1)), ' propo de victoire a domicile ' , get_moye_vict_domicile(int(eq1))*0.4
		print 'moyen is ' , (M[int(eq1)-1,int(eq2)-1]*0.6) + (get_moye_vict_domicile(int(eq1))*0.4)
		prop = (M[int(eq1)-1,int(eq2)-1]*0.6) + (get_moye_vict_domicile(int(eq1))*0.4) +(get_similarite(M,eq1-1)*0.6)
		dic['res'] = round(prop, 2)*100
		resu.append(dic)
	print 'end algo'
	return resu
	

def get_prediction(val1,val2):
	print 'call function '
	m = init_param_algo()
	res = prediction_algo(m,val1,val2)
	return res






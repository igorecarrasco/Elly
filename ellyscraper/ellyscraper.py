#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PARSE.LY API SCRAPER
"""
import urllib2
import oauth2
import json
import psycopg2
from pprint import pprint
import os
from os.path import join,dirname
from dotenv import load_dotenv

#load env path and file
dotenv_path = join(dirname(__file__),'..','.env')
load_dotenv(dotenv_path)

#load parameters from env file
token = os.getenv('parselytoken')
apikey= os.getenv('parselyapikey') 
db=os.getenv('db')
dbuser=os.getenv('dbuser')
dbpassword=os.getenv('dbpassword')
dbhost=os.getenv('dbhost')

#connect to db
conn = psycopg2.connect(database=db, user=dbuser, password=dbpassword, host=dbhost) 
cur = conn.cursor()

#Make API calls for top 20 posts in the last 24h and 48h 
umdia = 'http://api.parsely.com/v2/analytics/posts?apikey='+apikey+'&secret='+token+'&days=1&limit=15'
doisdia = 'http://api.parsely.com/v2/analytics/posts?apikey='+apikey+'&secret='+token+'&days=2&limit=15'
tresdia = 'http://api.parsely.com/v2/analytics/posts?apikey='+apikey+'&secret='+token+'&days=3&limit=15'

#capture 24h stats
response = urllib2.urlopen(umdia)
dados = json.load(response)['data']

#create clean list out of 24h data with only the things we need
#this was done to be able to compare lists as "Hits" field would yield different results
#thus making comparison impossible
listalimpa = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	listalimpa.append([title, tags, pubdate, link, thumb, authors, section])
	i=i+1

#repeat for 48h stats
response = urllib2.urlopen(doisdia)
dados = json.load(response)['data']

listalimpa2 = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	listalimpa2.append([title , tags , pubdate , link, thumb, authors, section])
	i=i+1

#repeat for 72h stats
response = urllib2.urlopen(tresdia)
dados = json.load(response)['data']

listalimpa3 = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	listalimpa3.append([title , tags , pubdate , link, thumb, authors, section])
	i=i+1

#compare lists and return only posts that were present in both 24h, 48h and 72h calls
novalista =[]
for element in listalimpa:
	if element in listalimpa2:
		if element in listalimpa3:
			novalista.append(element)

#start of section-specific calls - Life, 72h
sectioncall = 'http://api.parsely.com/v2/analytics/section/Life/detail?apikey='+apikey+'&secret='+token+'&days=3&limit=20'
response = urllib2.urlopen(sectioncall)
dados = json.load(response)['data']

lifelimpa1 = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	lifelimpa1.append([title , tags , pubdate , link, thumb, authors, section])
	i=i+1

#life - 48h
sectioncall = 'http://api.parsely.com/v2/analytics/section/Life/detail?apikey='+apikey+'&secret='+token+'&days=2&limit=20'
response = urllib2.urlopen(sectioncall)
dados = json.load(response)['data']

lifelimpa2 = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	lifelimpa2.append([title , tags , pubdate , link, thumb, authors, section])
	i=i+1

#for 24h
sectioncall = 'http://api.parsely.com/v2/analytics/section/Life/detail?apikey='+apikey+'&secret='+token+'&days=1&limit=20'
response = urllib2.urlopen(sectioncall)
dados = json.load(response)['data']

lifelimpa3 = []
i=0
while i<len(dados):
	title=dados[i]['title']
	tags=[]
	a=0
	while a<len(dados[i]['tags']): 
		tags.append(dados[i]['tags'][a])
		a=a+1
	pubdate=dados[i]['pub_date']
	link=dados[i]['link']
	thumb=dados[i]['image_url']
	authors=[]
	b=0
	while b<len(dados[i]['authors']): 
		authors.append(dados[i]['authors'][b])
		b=b+1
	section=dados[i]['section']
	lifelimpa3.append([title , tags , pubdate , link, thumb, authors, section])
	i=i+1

lifelista =[]
for element in lifelimpa1:
	if element in lifelimpa2:
		if element in lifelimpa3:
			lifelista.append(element)

for element in lifelista:
	novalista.append(element)

#write to the database title, tag list, published date, link, thumbnail url, author
#in the corresponding fields
i=0
while i<len(novalista):
	title=novalista[i][0]
	tags=novalista[i][1]
	pubdate=novalista[i][2]
	link=novalista[i][3]
	thumb=novalista[i][4]
	author=novalista[i][5]
	section=novalista[i][6]
	replace=["u'","'","[","]",'"']
	for a in replace:
		tags=str(tags).replace(a,"")
		author=str(author).replace(a,"")
		title=title.replace(a,"")
		section=section.replace(a,"")
	author = author.encode('utf_8')
	author = author.replace("’","'")
	title = title.encode('utf_8')
	title = title.replace("’","'")
	cur.execute("INSERT INTO elly_elly (title, tags, pubdate, link, thumb, author, section) VALUES (%s,%s,%s,%s,%s,%s,%s)",(title,tags,pubdate,link,thumb,author,section))
	i=i+1

cur.execute("DELETE FROM elly_elly WHERE id NOT IN (SELECT min(id) FROM elly_elly GROUP BY link)")

#commit
conn.commit()

#close cursor and connection with db
cur.close()
conn.close()

#it worked!
print "SUCESS"


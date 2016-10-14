#!/usr/bin/env python

"""
PARSE.LY API SCRAPER

"""
import urllib2
import oauth2
import json
import psycopg2
from pprint import pprint

#oath authentication (((old twitter scraper remnants)))
# def oauth_req(url,key,secret,http_method="GET",post_body="", http_headers=None):
# 	consumer = oauth2.Consumer(key='n2DCTtvbYs9Y7ItMu6TGdfIaI',secret='eDx3gC0Fyn873DAI3muGJqG7yV6GGyWvjDtBu4WEnxZblv8Zzf')
# 	token = oauth2.Token(key='291881212-ZbHxjlwr88tKZkxraLY4UXlvv1xDYuSPdosOIdCY',secret='BKCRNm4OKUXTxn304BUcddnF7n9BsrsmcD6Nq5ivXDEud')
# 	client = oauth2.Client(consumer,token)
# 	resp,content = client.request(url,method=http_method,body=post_body,headers=http_headers )
# 	return content

#Make API calls for top 5 posts in the last 24h and 48h 
umdia = 'http://api.parsely.com/v2/realtime/posts?apikey=blog.parsely.com&time=24h&limit=5'
doisdia = 'http://api.parsely.com/v2/realtime/posts?apikey=blog.parsely.com&time=48h&limit=5'

#capture 24h stats
response1 = urllib2.urlopen(umdia)
dados = json.load(response1)['data']

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
	thumb=dados[i]['thumb_url_medium']
	author=dados[i]['author']
	listalimpa.append([title , tags , pubdate , link, thumb, author])
	i=i+1

#repeat for 48h stats
response2 = urllib2.urlopen(doisdia)
dados2 = json.load(response2)['data']

listalimpa2 = []
i=0
while i<len(dados2):
	title=dados2[i]['title']
	tags=[]
	a=0
	while a<len(dados2[i]['tags']): 
		tags.append(dados2[i]['tags'][a])
		a=a+1
	pubdate=dados2[i]['pub_date']
	link=dados2[i]['link']
	thumb=dados2[i]['thumb_url_medium']
	author=dados2[i]['author']
	listalimpa2.append([title , tags , pubdate , link, thumb, author])
	i=i+1

#compare lists and return only posts that were present in both 24h and 48h calls
def equal_ignore_order(listalimpa, listalimpa2):
    unmatched = list(listalimpa2)
    for element in listalimpa:
        try:
            unmatched.remove(element)
        except ValueError:
            return False
    return not unmatched

#print final list
#pprint(listalimpa2)

#connect to db
conn = psycopg2.connect(database="djangotest", user="igorcarrasco")
cur = conn.cursor()

#create test table "tabelateste"
#cur.execute("CREATE TABLE IF NOT EXISTS tabelateste (id serial PRIMARY KEY, title varchar, tags varchar, pubdate varchar, link varchar, thumb varchar, author varchar);")

#write to the database title, tag list, published date, link, thumbnail url, author
#in the corresponding fields
i=0
while i<len(listalimpa2):
	title=listalimpa2[i][0]
	tags=listalimpa2[i][1]
	pubdate=listalimpa2[i][2]
	link=listalimpa2[i][3]
	thumb=listalimpa2[i][4]
	author=listalimpa2[i][5]
	cur.execute("INSERT INTO Elly (title, tags, pubdate, link, thumb, author) VALUES (%s,%s,%s,%s,%s,%s )",(title,tags,pubdate,link,thumb,author))
	i=i+1

#commit
conn.commit()

#recuperar todos os dados da table
cur.execute("SELECT * FROM Elly;")

#selecionar todos os dados da table testando
rows = cur.fetchall()

#imprimir o q tem na db
for row in rows:
	print row

#close cursor and connection with db
cur.close()
conn.close()

#it worked!
print "SUCESS"
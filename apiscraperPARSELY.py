#!/usr/bin/env python

"""
Test use of Twitter API for scraping #2

"""
import urllib2
import oauth2
import json
import psycopg2
from pprint import pprint

#autenticar oath
# def oauth_req(url,key,secret,http_method="GET",post_body="", http_headers=None):
# 	consumer = oauth2.Consumer(key='n2DCTtvbYs9Y7ItMu6TGdfIaI',secret='eDx3gC0Fyn873DAI3muGJqG7yV6GGyWvjDtBu4WEnxZblv8Zzf')
# 	token = oauth2.Token(key='291881212-ZbHxjlwr88tKZkxraLY4UXlvv1xDYuSPdosOIdCY',secret='BKCRNm4OKUXTxn304BUcddnF7n9BsrsmcD6Nq5ivXDEud')
# 	client = oauth2.Client(consumer,token)
# 	resp,content = client.request(url,method=http_method,body=post_body,headers=http_headers )
# 	return content

#acertando API calls para 24 e 48h 
umdia = 'http://api.parsely.com/v2/realtime/posts?apikey=blog.parsely.com&time=24h&limit=5'
doisdia = 'http://api.parsely.com/v2/realtime/posts?apikey=blog.parsely.com&time=48h&limit=5'

#capturar dados do dia 1
response1 = urllib2.urlopen(umdia)
dados = json.load(response1)['data']

#criar listalimpa com apenas os dados que nos precisaremos
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

#mesma coisa porem para 2 dias
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

#limpar lista dos elementos que nao estiverem nas duas
def equal_ignore_order(listalimpa, listalimpa2):
    unmatched = list(listalimpa2)
    for element in listalimpa:
        try:
            unmatched.remove(element)
        except ValueError:
            return False
    return not unmatched

#printar lista final 
#pprint(listalimpa2)
#conectar a db
conn = psycopg2.connect(database="djangotest", user="igorcarrasco")
cur = conn.cursor()

#criar tabela teste
cur.execute("CREATE TABLE IF NOT EXISTS tabelateste (id serial PRIMARY KEY, title varchar, tags varchar, pubdate varchar, link varchar, thumb varchar, author varchar);")

#escrever os valores 'text' (texto do twit) e 'id' (id do twit) para cada elemento da lista datafinal (variable i) 
#nos campos tweetid e data
i=0
while i<len(listalimpa2):
	title=listalimpa2[i][0]
	tags=listalimpa2[i][1]
	pubdate=listalimpa2[i][2]
	link=listalimpa2[i][3]
	thumb=listalimpa2[i][4]
	author=listalimpa2[i][5]
	cur.execute("INSERT INTO tabelateste (title, tags, pubdate, link, thumb, author) VALUES (%s,%s,%s,%s,%s,%s )",(title,tags,pubdate,link,thumb,author))
	i=i+1

#gravar
conn.commit()

#recuperar todos os dados da table
cur.execute("SELECT * FROM tabelateste;")

#selecionar todos os dados da table testando
rows = cur.fetchall()

#imprimir o q tem na db
for row in rows:
	print row

#fechar cursor
cur.close()
#fechar conexao com db
conn.close()
print "SUCESS"
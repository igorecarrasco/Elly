#!/usr/bin/env python

"""
Test use of API for scraping #2

"""
import urllib2
import oauth2
import json
import psycopg2
#from pprint import pprint

#autenticar oath
def oauth_req(url,key,secret,http_method="GET",post_body="", http_headers=None):
	consumer = oauth2.Consumer(key='n2DCTtvbYs9Y7ItMu6TGdfIaI',secret='eDx3gC0Fyn873DAI3muGJqG7yV6GGyWvjDtBu4WEnxZblv8Zzf')
	token = oauth2.Token(key='291881212-ZbHxjlwr88tKZkxraLY4UXlvv1xDYuSPdosOIdCY',secret='BKCRNm4OKUXTxn304BUcddnF7n9BsrsmcD6Nq5ivXDEud')
	client = oauth2.Client(consumer,token)
	resp,content = client.request(url,method=http_method,body=post_body,headers=http_headers )
	return content

#fazer request
user_timeline=oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=wsj&count=15', 'abcd', 'efgh') 
#carregar dados da timeline como json
data = json.loads(user_timeline)

#request numero dois-TL mais curta
user_timeline2=oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=wsj&count=5', 'abcd', 'efgh') 
#carregar dados 2 como json
data2 = json.loads(user_timeline2)

#obter lista coincidente como json
datafinal = [x for x in data if x in data2]

#conectar a db
conn = psycopg2.connect(database="djangotest", user="igorcarrasco")
cur = conn.cursor()

#criar tabela teste
#cur.execute("CREATE TABLE IF NOT EXISTS djangotest (id serial PRIMARY KEY, twitid varchar, texto varchar);")

#escrever os valores 'text' (texto do twit) e 'id' (id do twit) para cada elemento da lista datafinal (variable i) 
#nos campos tweetid e data
i=0
while i<len(datafinal):
	texto=datafinal[i]['text']
	numbero=datafinal[i]['id']
	cur.execute("INSERT INTO twitlister_tweet (twitid, texto) VALUES (%s,%s)",(json.dumps(numbero),json.dumps(texto)))
	i=i+1

#gravar
conn.commit()

#recuperar todos os dados da table
cur.execute("SELECT * FROM twitlister_tweet;")

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
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Elly
import re
import urllib2
import urllib
import json
import os
import random
import time
from os.path import join,dirname
from dotenv import load_dotenv
from django.utils.encoding import smart_str, smart_unicode
from requests_oauthlib import OAuth1Session, OAuth1
import requests

dotenv_path = join(dirname(__file__),'..','..','.env')
load_dotenv(dotenv_path)
token = os.getenv('parselytoken')
apikey= os.getenv('parselyapikey')
ckey = os.getenv('ckeysf')
csecret = os.getenv('csecretsf')
suid = os.getenv('serviceuserid')

request_token_url = 'https://www.socialflow.com/oauth/request_token?oauth_callback=oob'
oauth = OAuth1Session(ckey, client_secret=csecret)

fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

base_authorization_url = 'https://www.socialflow.com/oauth/authorize'

authorize_url = base_authorization_url + '?oauth_token='
authorize_url = authorize_url + resource_owner_key
print 'Please go her and authorize', authorize_url
verifier = raw_input('Plaese input the verifier')

access_token_url = 'https://www.socialflow.com/oauth/access_token'

oauth = OAuth1Session(ckey,
	client_secret=csecret,
	resource_owner_key=resource_owner_key,
	resource_owner_secret=resource_owner_secret,
	verifier=verifier)

oauth_tokens = oauth.fetch_access_token(access_token_url)

resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')

headeroauth = OAuth1(ckey,
	csecret,
	resource_owner_key,
	resource_owner_secret,
	signature_type='auth_header')

def index(request):
	elly_list = Elly.objects.order_by('-id')
	template = loader.get_template('elly/index.html')
	context = {'elly_list': elly_list,}
	return HttpResponse(template.render(context,request))

def socialflow(request):
	urlsocialflow = "https://api.socialflow.com/feed/list?account_type=twitter&limit=3&service_user_id="+suid
	r = oauth.get(urlsocialflow)
	return HttpResponse(r)

def rssfeed(request):
	if request.method == "POST":
		postids = request.POST.getlist('postid','')
		for element in postids:
			objetoelly = Elly.objects.get(id=element)
			titulo = objetoelly.title
			titulo = urllib.quote(titulo,safe= "")
			link = objetoelly.link
			urltwit = "https://api.socialflow.com/message/add?service_user_id="+suid+"&account_type=twitter&message="+titulo+" "+link+"&publish_option=hold&shorten_links=1"
			r = oauth.get(urltwit)
	# 	f=open('elly/rssfeed.rss','w')
	# 	f.write('<?xml version="1.0" encoding="UTF-8"?><channel><title>Weekend Social Scheduling - Tweets</title><link>http://online.wsj.com/page/2_0062.html</link><atom:link type="application/rss+xml" rel="self" href="http://online.wsj.com/page/2_0062.html"/><description>Social Headlines for Methode Articles</description><language>en-us</language><pubDate>Wed, 02 Nov 2016 18:19:52 -0400</pubDate><lastBuildDate>Wed, 02 Nov 2016 18:19:52 -0400</lastBuildDate><copyright>Dow Jones &amp; Company, Inc.</copyright><generator>http://online.wsj.com/page/2_0062.html</generator><docs>http://cyber.law.harvard.edu/rss/rss.html</docs><image><title>Social Headlines for Methode Articles</title><link>http://online.wsj.com/page/2_0062.html</link><url>http://online.wsj.com/img/wsj_sm_logo.gif</url></image>')
	# postids = request.POST.getlist('postid','')
	# for element in postids:
	# 	objetoelly = Elly.objects.get(id=element)
	# 	titulo = objetoelly.title
	# 	f.write('<item><title>'+titulo+'</title><link>'+objetoelly.link+'</link><description><![CDATA[]]></description><content:encoded/><pubDate><![CDATA[]]></pubDate><guid isPermaLink="false"><![CDATA[]]></guid><category domain="AccessClassName">FREE</category></item>')
	# 	f.write('</channel></rss>')
	template = loader.get_template('elly/rssfeed.html')
	context = {'postids':postids,}
  	return HttpResponse(template.render(context,request))

def hits(request):
	if request.method == "POST":
		urlitem = request.body
		urlhits = "http://api.parsely.com/v2/analytics/post/detail?apikey="+apikey+"&secret="+token+"&url="+urlitem
		respostahits = urllib2.urlopen(urlhits)
		hits = json.load(respostahits)['data'][0]['visitors']
		return HttpResponse(hits)

def likes(request):
	if request.method == "POST":
		urlitem = request.body		
		urllikes = "http://api.parsely.com/v2/shares/post/detail?apikey="+apikey+"&secret="+token+"&url="+urlitem
		respostalikes = urllib2.urlopen(urllikes)
		likes = json.load(respostalikes)['data'][0]['fb']
		return HttpResponse(likes)

def rts(request):
	if request.method == "POST":
		urlitem = request.body		
		urlrts = "http://api.parsely.com/v2/shares/post/detail?apikey="+apikey+"&secret="+token+"&url="+urlitem
		respostarts = urllib2.urlopen(urlrts)
		rts = json.load(respostarts)['data'][0]['tw']
		return HttpResponse(rts)

def filter (request):
	if request.method == "GET":
		filteredposts = request.GET.get('filter','')
		filtered_list=Elly.objects.filter(section=filteredposts)
		template = loader.get_template('elly/index.html')
		context = {'elly_list': filtered_list,}
		return HttpResponse(template.render(context,request))

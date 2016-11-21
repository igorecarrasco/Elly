# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
from django.core.urlresolvers import reverse
from django.contrib.postgres.search import SearchVector
import requests
import datetime
from datetime import timedelta


dotenv_path = join(dirname(__file__),'..','..','.env')
load_dotenv(dotenv_path)
token = os.getenv('parselytoken')
apikey= os.getenv('parselyapikey')
ckey = os.getenv('ckeysf')
csecret = os.getenv('csecretsf')
# suid = os.getenv('serviceuserid')

access_token_url = 'https://www.socialflow.com/oauth/access_token'
base_authorization_url = 'https://www.socialflow.com/oauth/authorize'

def login(request):
	#first steps of oauth1 login
	urlcallback = request.build_absolute_uri(reverse('login2'))
	request_token_url = 'https://www.socialflow.com/oauth/request_token'+ '?oauth_callback=' + urlcallback
	oauth = OAuth1Session(ckey, client_secret=csecret)
	fetch_response = oauth.fetch_request_token(request_token_url)
	resource_owner_key = fetch_response.get('oauth_token')
	resource_owner_secret = fetch_response.get('oauth_token_secret')
	request.session['resource_owner_key'] = resource_owner_key
	request.session['resource_owner_secret'] = resource_owner_secret
	authorize_url = base_authorization_url + '?oauth_token=' 
	authorize_url = authorize_url + resource_owner_key + '&oauth_callback=' + urlcallback
	#drive user to lister view, where rest of authorization can take place
	return HttpResponseRedirect(authorize_url)

def login2(request):
	urlcallback = request.build_absolute_uri(reverse('lister'))
	verifier = request.GET.get('oauth_verifier')
	request.session['verifier'] = verifier
	resource_owner_key = request.GET.get('oauth_token')
	request.session['resource_owner_key'] = resource_owner_key
	resource_owner_secret = request.session['resource_owner_secret']
	oauth = OAuth1Session(ckey,
		client_secret=csecret,
		resource_owner_key=resource_owner_key,
		resource_owner_secret=resource_owner_secret,
		verifier=verifier)
	oauth_tokens = oauth.fetch_access_token(access_token_url)
	resource_owner_key = oauth_tokens.get('oauth_token')
	resource_owner_secret = oauth_tokens.get('oauth_token_secret')
	request.session['resource_owner_key'] = resource_owner_key
	request.session['resource_owner_secret'] = resource_owner_secret
	return HttpResponseRedirect(urlcallback)

def lister(request):
	elly_list = Elly.objects.order_by('-id')
	template = loader.get_template('elly/index.html')
	context = {'elly_list': elly_list,}
	return HttpResponse(template.render(context,request))

def socialflow(request):
	resource_owner_secret = request.session['resource_owner_secret']
	verifier = request.session['verifier']
	resource_owner_key = request.session['resource_owner_key']
	headeroauth = OAuth1(ckey,
		csecret,
		resource_owner_key,
		resource_owner_secret,
		signature_type='auth_header')
	urlsocialflow = "https://api.socialflow.com/account/list?&account_type=twitter,facebook_page&limit=5"
	r = requests.get(urlsocialflow,auth=headeroauth)
	return HttpResponse(r)

def postsocial(request):
	resource_owner_secret = request.session['resource_owner_secret']
	verifier = request.session['verifier']
	resource_owner_key = request.session['resource_owner_key']
	headeroauth = OAuth1(ckey,
		csecret,
		resource_owner_key,
		resource_owner_secret,
		signature_type='auth_header')
	if request.method == "POST":
		postids = request.POST.getlist('postid','')
		schedtype = request.POST.get('schedtype','')
		account = request.POST.get('accountselector','')
		accountdata = account.replace(' ','').split(',')
		socialtype = accountdata[0]
		suid = accountdata[1]
		optimizestartdate=""
		optimizeenddate=""
		scheduledt=""
		if schedtype == 'optimize':
			schedtime = request.POST.get('schedtime','')
			schedtime = int(schedtime)
			# now = datetime.datetime.now()
			# startdate = now.strftime("%Y-%m-%d %H:%M:%S")
			startdate = request.POST.get('startoptdatetime','')
			startdatedt = datetime.datetime.strptime(startdate,"%Y-%m-%d %H:%M:%S")
			enddate=startdatedt+timedelta(hours=schedtime)
			enddate = enddate.strftime("%Y-%m-%d %H:%M:%S")
			optimizestartdate = "&optimize_start_date="+startdate
			optimizeenddate = "&optimize_end_date="+enddate
		elif schedtype == 'schedule':
			scheddatetime = request.POST.get('scheduletime','')
			scheduledt = "&scheduled_date="+scheddatetime
		listtitles = []
		for element in postids:
			objetoelly = Elly.objects.get(id=element)
			titulo = objetoelly.socialhed
			if titulo == "":
				titulo = objetoelly.title
			if objetoelly.section == "Opinion":
				titulo.append("via @WSJOpinion")
			titulo = titulo.encode('utf8')
			titulo = urllib.quote(titulo,safe= "")
			link = objetoelly.link
			urltwit = "https://api.socialflow.com/message/add?service_user_id="+suid+"&account_type="+socialtype+"&message="+titulo+" "+link+"&publish_option="+schedtype+scheduledt+optimizestartdate+optimizeenddate+"&shorten_links=1"
			listtitles.append(objetoelly.title)
			r = requests.get(urltwit,auth=headeroauth)
	template = loader.get_template('elly/rssfeed.html')
	context = {'listtitles':listtitles,}
  	return HttpResponse(template.render(context,request))

# Start of views related to loading analytics to the lister page
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

#start of views related to searching and sorting 
def filter (request):
	if request.method == "GET":
		filteredposts = request.GET.get('filter','')
		filtered_list=Elly.objects.filter(section=filteredposts)
		template = loader.get_template('elly/index.html')
		context = {'elly_list': filtered_list,}
		return HttpResponse(template.render(context,request))

def search (request):
	if request.method == "GET":
		searchobject = request.GET.get('search','')
		searched_list = Elly.objects.annotate(search=SearchVector('tags', 'title'),
			).filter(search=searchobject)
		print searched_list
		template = loader.get_template('elly/index.html')
		context = {'elly_list': searched_list,}
		return HttpResponse(template.render(context,request))

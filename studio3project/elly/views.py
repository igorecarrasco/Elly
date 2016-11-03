# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Elly
from django.http import HttpResponseRedirect
from django.utils import feedgenerator
import re
import urllib2
import json
import os
from os.path import join,dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__),'..','..','.env')
load_dotenv(dotenv_path)
token = os.getenv('parselytoken')
apikey= os.getenv('parselyapikey')

def index(request):
	elly_list = Elly.objects.order_by('-id')
	template = loader.get_template('elly/index.html')
	context = {'elly_list': elly_list,}
	return HttpResponse(template.render(context,request))

def rssfeed(request):
  if request.method == "POST":
  	f=open('elly/rssfeed.rss','w')
  	f.write('<?xml version="1.0" encoding="UTF-8"?><channel><title>Weekend Social Scheduling - Tweets</title><link>http://online.wsj.com/page/2_0062.html</link><atom:link type="application/rss+xml" rel="self" href="http://online.wsj.com/page/2_0062.html"/><description>Social Headlines for Methode Articles</description><language>en-us</language><pubDate>Wed, 02 Nov 2016 18:19:52 -0400</pubDate><lastBuildDate>Wed, 02 Nov 2016 18:19:52 -0400</lastBuildDate><copyright>Dow Jones &amp; Company, Inc.</copyright><generator>http://online.wsj.com/page/2_0062.html</generator><docs>http://cyber.law.harvard.edu/rss/rss.html</docs><image><title>Social Headlines for Methode Articles</title><link>http://online.wsj.com/page/2_0062.html</link><url>http://online.wsj.com/img/wsj_sm_logo.gif</url></image>')
	postids = request.POST.getlist('postid','')
	for element in postids:
		objetoelly = Elly.objects.get(id=element)
  		f.write('<item><title>'+objetoelly.title+'</title><link>'+objetoelly.link+'</link><description><![CDATA[]]></description><content:encoded/><pubDate><![CDATA[]]></pubDate><guid isPermaLink="false"><![CDATA[]]></guid><category domain="AccessClassName">FREE</category></item>')
  	f.write('</channel></rss>')
  	elly_list = Elly.objects.order_by('id')
  	template = loader.get_template('elly/index.html')
	context = {'elly_list': elly_list,}
  	return HttpResponse(template.render(context,request))

def hits(request):
	if request.method == "POST":
		urlitem = request.body
		url = "http://api.parsely.com/v2/analytics/post/detail?apikey="+apikey+"&secret="+token+"&url="+urlitem
		resposta = urllib2.urlopen(url)
		hits = json.load(resposta)['data'][0]['visitors']
		return HttpResponse(hits)
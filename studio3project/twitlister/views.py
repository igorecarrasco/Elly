from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Tweet

def index(request):
	latest_twit_list = Tweet.objects.order_by('id')
	template = loader.get_template('twitlister/index.html')
	context = {'latest_twit_list': latest_twit_list,}
	return HttpResponse(template.render(context,request))
#output = '<br>'.join([q.texto+"  "+q.twitid for q in latest_twit_list])
#return HttpResponse(output)

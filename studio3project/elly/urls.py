from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'lister', views.lister, name='lister'),
    url(r'posttweets', views.posttweets),
    url(r'hits', views.hits),
    url(r'likes', views.likes),
    url(r'rts', views.rts),
    url(r'filter', views.filter),
    url(r'socialflow',views.socialflow)
]
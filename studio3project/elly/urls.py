from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'rssfeed', views.rssfeed),
    url(r'hits', views.hits),
    url(r'likes', views.likes),
    url(r'rts', views.rts),
    url(r'filter', views.filter),
    url(r'socialflow',views.socialflow)
]
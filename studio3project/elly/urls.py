from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'login2', views.login2, name='login2'),
    url(r'index', views.index, name='index'),
    url(r'postsocial', views.postsocial),
    url(r'hits', views.hits),
    url(r'likes', views.likes),
    url(r'rts', views.rts),
    url(r'filter', views.filter),
    # url(r'pubdate', views.pubdate),
    url(r'socialflow',views.socialflow),
    url(r'search',views.search),
]
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^index_blog/$', views.index_blog, name='index_blog'),
    
    url(r'^index_gifscreen/$', views.index_gifscreen, name='index_gifscreen'),
]

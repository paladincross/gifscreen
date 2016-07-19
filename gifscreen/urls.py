from django.conf.urls import include, url 

import django.contrib.auth.views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import admin

admin.autodiscover()



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    
    url(r'', include('blog.urls')),
]

from django.conf.urls import include, url, patterns

import django.contrib.auth.views

from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib import admin

from . import views

admin.autodiscover()


from django.views.generic.base import TemplateView

urlpatterns = [
    
   #url(r'', 'home.views.index'),

    url(r'', include('blog.urls')),

    url(r'', include('home.urls')),

    url(r'', include('screen.urls')),
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),

    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '^bloghome/'}),

]

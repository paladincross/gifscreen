from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^screen/$', views.screen_home, name='screen_home'),

]

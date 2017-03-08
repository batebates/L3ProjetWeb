from django.conf.urls import include, url
from . import views

app_name = "room"

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<idRoom>[0-9]{1,3})/$', views.detail, name='detail'),
	url(r'^(?P<idRoom>[0-9]+)/creation/$', views.creation, name='creation')
]

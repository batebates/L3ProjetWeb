from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    url(r'^inscription$', views.inscription, name='inscription'),
    url(r'^password_forget$', views.password_forget,name='password_forget'),
    url(r'^profil$', views.profil,name='profil'),
    url(r'^$', views.index, name='index'),
]

from django.db import models
	
class Question(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.CharField(max_length=20)

class Reponse(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.CharField(max_length=20)

class Utilisateur(models.Model):
	pseudo = models.CharField(max_length=20)
	mdp = models.CharField(max_length=32)
	mail = models.CharField(max_length=20)

class Amis(models.Model):
	utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE, related_name='%(class)s_base')
	amisde = models.ForeignKey(Utilisateur, related_name='%(class)s_ami')
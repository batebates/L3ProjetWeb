from django.db import models

class Utilisateur(models.Model):
	pseudo = models.CharField(max_length=12)
	mdp = models.CharField(max_length=12)
	mail = models.CharField(max_length=20)

class Amis(models.Model):
	utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
	amisde = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

	
class Question(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
	

class Reponse(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
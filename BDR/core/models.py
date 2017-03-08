from django.db import models

STATUT_CHOIX = (
    ('b', 'Brouillon'),
    ('p', 'Publiée'),
    ('r', 'Retirée'),
)

class Question(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.CharField(max_length=20)
	statut = models.CharField(max_length=1, choices=STATUT_CHOIX)


class Reponse(models.Model):
	intitule = models.CharField(max_length=200)
	utilisateur = models.CharField(max_length=20)
	statut = models.CharField(max_length=1, choices=STATUT_CHOIX)

class Utilisateur(models.Model):
	pseudo = models.CharField(max_length=20)
	mdp = models.CharField(max_length=32)
	mail = models.CharField(max_length=20)

class Amis(models.Model):
	utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE, related_name='%(class)s_base')
	amisde = models.ForeignKey(Utilisateur, related_name='%(class)s_ami')
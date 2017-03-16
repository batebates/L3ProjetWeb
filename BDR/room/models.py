from django.db import models
from core.models import Question,Reponse
from django.contrib.auth.models import User


class Room(models.Model):
	roomIsOpen = models.BooleanField()
	roomName = models.CharField(
        max_length=64,
    )

class RoomMember(models.Model):
	membre = models.OneToOneField(User)
	room = models.IntegerField()
	chef = models.BooleanField()
	question = models.ForeignKey(Question,null=True)
	score = models.IntegerField()
	reponse = models.ForeignKey(Reponse,null=True)
	etat = models.IntegerField(null=True)

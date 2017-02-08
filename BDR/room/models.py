from django.db import models

class Room(models.Model):
	roomIsOpen = models.BooleanField()
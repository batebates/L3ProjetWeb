from django.db import models

class Room(models.Model):
	roomIsOpen = models.BooleanField()
	roomName = models.CharField(
        max_length=64,
    )
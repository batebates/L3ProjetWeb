from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render

from room.models import Room

def index(request):
	context = ""
	return render(request, 'room/index.html', context)

def detail(request, idRoom):
	try:
		room = Room.objects.get(pk=idRoom)
		return HttpResponse("Welcome to room %s !" % idRoom)
	except Room.DoesNotExist:
		return HttpResponse("Room does not exist yet")
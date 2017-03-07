from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

from room.models import Room

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True)
	return render(request, 'core/index.html', {'rooms' : open_rooms_list})

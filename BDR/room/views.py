from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

from room.models import Room

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True).order_by('id')
	return render(request, 'room/index.html', {'openRooms' : open_rooms_list})

def detail(request, idRoom):
	try:
		room = Room.objects.get(pk=idRoom)
		return render(request, 'room/roomOpen.html', {'room':room})
	except Room.DoesNotExist:
		context = ""
		return render(request, 'room/noRoom.html', {'idRoom':idRoom})


@csrf_protect
def creation(request, idRoom):
	csrfContext = RequestContext(request, idRoom)
	try:
		room = Room.objects.get(pk=idRoom)
		return render(request, 'room/roomOpen.html', csrfContext, {'room':room})
	except Room.DoesNotExist:
		room = Room()
		room.pk=idRoom
		room.roomIsOpen=True
		room.save()
		return HttpResponseRedirect(reverse('room:detail', args=[idRoom]))

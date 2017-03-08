from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

from room.models import Room

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True).order_by('id')[:5]
	first_closed_room = open_rooms_list.reverse().first()
	if first_closed_room :
		first_closed_room_id = first_closed_room.id + 1
	else :
		first_closed_room_id = 1
	
	return render(request, 'core/index.html', {'openRooms' : open_rooms_list, 'closedRoomId' : first_closed_room_id})
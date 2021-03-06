from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse

from django.db.models.aggregates import Count
from random import randint

from room.models import Room
from core.models import Question, Reponse

def random(self):
	count = self.filter(statut='p').aggregate(count=Count('id'))['count']
	
	if count > 0 :
		random_index = randint(0, count - 1)
		return self.all()[random_index]
	else :
		return None
	

def randomIterable(self, nbObj):
	listeRetour = []

	count = self.aggregate(count=Count('id'))['count']

	listeChoix = self

	for i in range(0,nbObj) :
		retour = random(listeChoix)
		if retour :
			listeChoix = listeChoix.exclude(id=retour.id)
			listeRetour.append(retour)

	return listeRetour

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True).order_by('id')
	return render(request, 'room/index.html', {'openRooms' : open_rooms_list})

def detail(request, idRoom):
	try:
		room = Room.objects.get(pk=idRoom)
		questionAEnvoyer = random(Question.objects.all())
		reponses = randomIterable(Reponse.objects.all(), 4)
		
		return render(request, 'room/roomOpen.html', {'room':room, 'question':questionAEnvoyer, 'reponses':reponses})
		
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

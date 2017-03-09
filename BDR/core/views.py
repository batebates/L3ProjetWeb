# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from .forms import PasswordForgetForm
from room.models import Room
import re

def validateEmail(email):
    if len(email) > 6:
        if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', email) != None:
            return 1
    return 0

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True).order_by('id')[:5]
	first_closed_room = open_rooms_list.reverse().first()
	if first_closed_room :
		first_closed_room_id = first_closed_room.id + 1
	else : # Si aucune salle n'est ouverte
		first_closed_room_id = 1

	return render(request, 'core/index.html', {'openRooms' : open_rooms_list, 'closedRoomId' : first_closed_room_id})
from django.contrib.auth import authenticate, login

def connexion(request):
	message_error = None
	if request.method == "POST":
		form = request.POST

	if form["password"] is None:
		message_error = "Le mot de passe n'a pas été indiqué"
		return redirect('index')

	if form["pseudo"] is None:
		message_error = "Le pseudo n'a pas été indiqué"
		return redirect('index')

	username = form["pseudo"]
	password = form["password"]
	user = authenticate(username=username, password=password)
	if user:
		login(request, user)
	else:
		error = "Les identifiants sont incorrects"
	return redirect('index')

from django.contrib.auth import logout
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

from django.contrib.auth.models import User

def inscription(request):
    message_error = None
    if request.method == "POST":
        form = request.POST
        if(form["password"] != form["confirm-password"]):
            message_error = "Les mots de passe doivent être identiques"
            return redirect('index')
        if validateEmail(form["email"]) is False:
            message_error = "Email invalide"
            return redirect('index')
        else:
            username = form["pseudo"]
            password = form["password"]
            email = form["email"]
            user = User.objects.create_user(username,email,password)
        if user:  # Si l'objet renvoye n'est pas None
            login(request, user)  # nous connectons l'utilisateur
        else: # sinon une erreur sera affichee
            message_error = "Erreur d'inscription"
    else:
        form = ConnexionForm()
    return redirect('index')


def password_forget(request):
	error = False
	if request.method == "POST":
		form = PasswordForgetForm(request.POST)
	else:
		form = PasswordForgetForm()
	return render(request,'core/password_forget.html',locals())

def profil(request):
	error = False
	user = request.user
	if request.method == "POST":
		form = request.POST
		if form:
			user.first_name = form["prenom"]
			user.last_name = form["nom"]
			user.email = form["email"]
			user.save()
	return render(request,'core/profil.html',locals())

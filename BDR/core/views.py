from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from .forms import PasswordForgetForm
from room.models import Room

def index(request):
	open_rooms_list = Room.objects.filter(roomIsOpen=True).order_by('id')[:5]
	first_closed_room = open_rooms_list.reverse().first()
	if first_closed_room :
		first_closed_room_id = first_closed_room.id + 1
	else :
		first_closed_room_id = 1

	return render(request, 'core/index.html', {'openRooms' : open_rooms_list, 'closedRoomId' : first_closed_room_id})
from django.contrib.auth import authenticate, login

def connexion(request):
    error = False
    if request.method == "POST":
        form = request.POST
        if form:
            username = form["pseudo"]
            password = form["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True

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
	error = False
	if request.method == "POST":
		form = request.POST
		if(form["password"] != form["confirm-password"]):
			#request.add_error('confirm-password', _("You must type the same password each time."))
			error = True
			return redirect('index')
		else:
			username = form["pseudo"]
			password = form["password"]
			email = form["email"]
			user = User.objects.create_user(username,email,password)
			if user:  # Si l'objet renvoye n'est pas None
				login(request, user)  # nous connectons l'utilisateur
			else: # sinon une erreur sera affichee
				error = True
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

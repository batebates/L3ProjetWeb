from channels import Channel,Group
from channels.sessions import channel_session, enforce_ordering
from channels.auth import channel_session_user, channel_session_user_from_http
from room.models import RoomMember
from core.models import Reponse,Question
from django.core  import serializers
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from random import randint
import json
# Connected to websocket.connect
def random(self):
	count = self.aggregate(count=Count('id'))['count']
	random_index = randint(0, count - 1)

	return self.all()[random_index]

def randomIterable(self, nbObj):
	listeRetour = []

	count = self.aggregate(count=Count('id'))['count']

	listeChoix = self

	for i in range(0,nbObj) :
		retour = random(listeChoix)
		listeChoix = listeChoix.exclude(id=retour.id)
		listeRetour.append(retour)

	return listeRetour

@channel_session_user_from_http
def ws_add(message):
    nbrCo = 4
    #RoomMember.objects.filter(room=int(message.content['path'].replace("""/room/""",""))).annotate(Count("membre"))[0]
    valRoom = "Room-" + message.content['path'].replace("""/room/""","")
    print(message.user)
    if(nbrCo<5):
        message.reply_channel.send({"accept": True})
        Group(valRoom).add(message.reply_channel)
        #RoomMember.objects.create(membre = message.user, room =1, chef = False, question = None,reponse = None, score = 0, etat = 0).save()
        joueur = RoomMember.objects.get(membre = message.user)
        if joueur:
            joueur.room = 1
            joueur.chef = False
            joueur.question = None
        else:
            joueur = RoomMember.objects.create(membre = message.user, room =1, chef = False, question = None,reponse = None, score = 0, etat = 0).save()


    if(nbrCo==4):
        joueur.question = random(Question.objects.all())
        joueur.etat = 0
        joueur.save()
        tab = RoomMember.objects.filter(room = 1)
        tab[0].chef = True
        for joueurs in tab:
            joueurs.question = joueur.question
            joueurs.save()
        donnee = {
                "question": joueur.question.intitule,
                "etat":joueur.etat,
                "master" : 0,
                "score":[tab[0].score,tab[1].score,tab[2].score,tab[3].score],
                "joueur":[tab[0].membre.username,tab[1].membre.username,tab[2].membre.username,tab[3].membre.username]
        }

        Group(valRoom).send({"text":json.dumps(donnee)})
        # Accept the socket




# Connected to websocket.receive
@channel_session_user
def ws_receive(message):
    #Si Joueur inscription de la reponse + requete pour lui dire d'attendre
    #Si maitre inscription du gagnant + requete pour regenerer une prochaine partie
    valRoom = "Room-" + message.content['path'].replace("""/room/""","")
    data = json.loads(message.content["text"])
    joueur = RoomMember.objects.get(membre = message.user)
    if joueur.chef == False:
        joueur.reponse = Reponse.objects.get(intitule = data['reponse'])
        joueur.etat = 1
        joueur.save()
        tab = RoomMember.objects.filter(room = 1)
        donnee = {
            "question": joueur.question.intitule,
            "etat":joueur.etat,
            "master" : 0,
            "score":[tab[0].score,tab[1].score,tab[2].score,tab[3].score],
            "joueur":[tab[0].membre.username,tab[1].membre.username,tab[2].membre.username,tab[3].membre.username]
            }
        message.reply_channel.send({"text":json.dumps(donnee)})
    else:
        reponseGagnante=joueur.reponse
        joueur.chef = False
        joueur.reponse = None
        listeDesGagnants = RoomMember.objects.filter(reponse = reponseGagnante)
        for joueurGagnant in listeDesGagnants:
            joueurGagnant.score +=1
            joueurGagnant.save()
        listeDesGagnants[0].chef = True
        listeDesGagnants[0].save()
        joueur.question = random(Question.objects.all())
        joueur.etat = 0
        joueur.save()
        tab = RoomMember.objects.filter(room = 1)
        tab[0].chef = True
        for joueurs in tab:
            joueurs.question = joueur.question
            joueurs.save()
        donnee = {
                "question": joueur.question.intitule,
                "etat":joueur.etat,
                "master" : 0,
                "score":[tab[0].score,tab[1].score,tab[2].score,tab[3].score],
                "joueur":[tab[0].membre.username,tab[1].membre.username,tab[2].membre.username,tab[3].membre.username]
        }

        Group(valRoom).send({"text":json.dumps(donnee)})

    #RoomMember.objects.filter(membre = User).reponse = message.content['text']
    # Without enforce_ordering this wouldn't work right
    # message.channel_session['sent'] = message.channel_session['sent'] + 1
    # Group("chat").send({
    #     "text": "%s: %s" % (message.channel_session['sent'], message.content['text']),
    # })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("jeu").discard(message.reply_channel)
    #RoomMember.objects.filter(membre =  User).delete()

def tableauScore(data):
    tab = RoomMember.objects.filter(room = data['room'])
    Group("jeu").send(json.dumps(tab))

def reponseTourMaitreJeu(message):
    tab = RoomMember.objects.filter(room = data['room'])
    Group("jeu").send(json.dumps(tab))

def reponseTour(message):
    tab = RoomMember.objects.filter(room = data['room'])
    Group("jeu").send(json.dumps(tab))

from django.contrib import admin
from .models import Question, Reponse

def publier(modeladmin, request, queryset):
    queryset.update(statut='p')
publier.short_description = "Rendre l'objet utilisable par les joueurs"

def retirer(modeladmin, request, queryset):
    queryset.update(statut='r')
retirer.short_description = "Rendre l'objet indispobible pour les joueurs"

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['id', 'intitule', 'utilisateur', 'statut']
	ordering = ['id']
	actions = [publier, retirer]

class ReponseAdmin(admin.ModelAdmin):
	list_display = ['id', 'intitule', 'utilisateur', 'statut']
	ordering = ['id']
	actions = [publier, retirer]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse, ReponseAdmin)
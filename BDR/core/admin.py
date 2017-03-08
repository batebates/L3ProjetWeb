from django.contrib import admin

from .models import Question, Reponse

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['id', 'intitule', 'utilisateur']
	ordering = ('id',)

class ReponseAdmin(admin.ModelAdmin):
	list_display = ['id', 'intitule', 'utilisateur']
	ordering = ('id',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Reponse, ReponseAdmin)
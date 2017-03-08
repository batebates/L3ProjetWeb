from django import forms

class CreationForm(forms.Form):
	salleNumero = forms.DecimalField(max_digits=3, decimal_places=0)
    salleNom = forms.CharField(label="Nom de la salle", max_length=30)
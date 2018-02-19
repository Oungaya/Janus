from django import forms
from .models import Parcours

class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))

class InscriptionForm(forms.Form):
    queryParcours = Parcours.objects.all()
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    numero_etudiant = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    parcours = forms.ModelChoiceField(queryset=queryParcours,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))
    confirmPassword = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    telephone = forms.IntegerField(max_value=99999999999,widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}))
    ajac = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))
    redoublant = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))

class MpoublieForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))

class ReinitialisationForm(forms.Form):
    confirmPassword = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))
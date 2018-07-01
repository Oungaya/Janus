from django import forms
from .models import Parcours, Statut
from django.contrib.auth.models import Group


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
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    #AJAC plus pris en compte dans l'inscription mais dans la validation admin de l'étudiant (MAJ du 13-03-2018)
    #ajac = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))
    redoublant = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))

class InscriptionProfesseurForm(forms.Form):
    queryStatut = Statut.objects.all()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    #nombre_heures = forms.IntegerField(max_value=99999999999,widget=forms.NumberInput(attrs={'class' : 'mdl-textfield__input'}))
    statut = forms.ModelChoiceField(queryset=queryStatut,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    notifierParMail = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))


class InscriptionAdminForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    #isProf = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))

class AjoutPeriodeForm(forms.Form):
    queryParcours = Parcours.objects.all()
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    parcours = forms.ModelChoiceField(queryset=queryParcours,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    dateDebutS1 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateDebutS2 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateFinS1 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateFinS2 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateDebutOptionsS1 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateDebutOptionsS2 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateFinOptionsS1 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    dateFinOptionsS2 = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    date_debut_annee = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))
    date_fin_annee = forms.DateTimeField(widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom'}))

class ModificationPeriodeForm(forms.Form):
    queryParcours = Parcours.objects.all()
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    parcours = forms.ModelChoiceField(queryset=queryParcours, widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    dateDebutS1 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateDebutS2 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateFinS1 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateFinS2 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateDebutOptionsS1 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateDebutOptionsS2 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateFinOptionsS1 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    dateFinOptionsS2 = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input date-field-custom', 'type' : 'date-local'}))
    date_debut_annee = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input datetime-field-custom', 'type' : 'datetime-local'}))
    date_fin_annee = forms.DateTimeField(input_formats='%d/%m/%Y', widget=forms.DateInput(attrs={'class' : 'mdl-textfield__input datetime-field-custom', 'type' : 'datetime-local'}))

class ModificationAdminForm(forms.Form):
    queryGroupe = Group.objects.all()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    #groupe = forms.ModelChoiceField(queryset=queryGroupe,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    #isProf = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}))

class ModificationProfByAdminForm(forms.Form):
    queryStatut = Statut.objects.all()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    statut = forms.ModelChoiceField(queryset=queryStatut,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))

class MpoublieForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))

class ReinitialisationForm(forms.Form):
    confirmPassword = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'mdl-textfield__input'}))


class ValidationUserByAdminForm(forms.Form):
    queryParcours = Parcours.objects.all()
    nom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    prenom = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    numero_etudiant = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    parcours = forms.ModelChoiceField(queryset=queryParcours,widget=forms.Select(attrs={'class' : 'mdl-textfield__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'mdl-textfield__input'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'mdl-textfield__input'}))
    ajac = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}), required = False)
    redoublant = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'mdl-switch__input'}), required = False)
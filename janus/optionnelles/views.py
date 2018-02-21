from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import Etudiant, Professeur, Parcours
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.template.context_processors import csrf
from .forms import ConnexionForm, InscriptionForm, InscriptionProfesseurForm, MpoublieForm, ReinitialisationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .optionnellesHelpers import getGroupTemplate
from django.contrib.auth.models import Group
from django.contrib import messages
import random, string

def generer_mdp():
    length = 8
    mdp = []
    mdp.append(random.choice(string.ascii_lowercase))
    mdp.append(random.choice(string.ascii_uppercase))
    mdp.append(str(random.randint(0,9)))
    random.shuffle(mdp)
    return ''.join(mdp)

@login_required
def index(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/index.html', context)

@login_required
def admin_ValidationInscription(request):
    liste_etudiant = Etudiant.objects.filter(utilisateur__is_active=False)
    context = {
        'liste_etudiant': liste_etudiant,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/validation_inscription_admin.html', context)

@login_required
def admin_InscriptionProfesseur(request):
    user_list = User.objects.all()
    professeur_list = Professeur.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }
    print(context)
    if request.method == 'POST':
        form = InscriptionProfesseurForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            djangoUser = User.objects.create_user(username=data['prenom'][0].lower()+data['nom'].lower(), email=data['email'], password=generer_mdp())
            my_group = Group.objects.get(name='Professeur') 
            my_group.user_set.add(djangoUser)
            djangoUser.first_name = username=data['prenom']
            djangoUser.last_name = username=data['nom']
            djangoUser.is_active = "True"
            djangoUser.save()
            professeurUser = Professeur(nombre_heures=data['nombre_heures'])
            professeurUser.utilisateur = djangoUser
            professeurUser.save()
            messages.success(request, 'Le professeur a été ajouté')
            return HttpResponseRedirect('/options/')
        else:
            raise forms.ValidationError(
                    "Votre compte n'a pas encore été activé ou a été désactivé "
                    )
    else:
        form = InscriptionProfesseurForm()
    print(context)
    return render(request, 'optionnelles/inscription_professeur_admin.html', {'form': form,'user_list': user_list,'template_group': getGroupTemplate(request.user)})

@login_required
def user_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user': user,
    }
    return render(request, 'optionnelles/user.html', context)


def user_connection(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/options/')
                else:
                    form.add_error(None,
                    "Votre compte n'a pas encore été activé ou a été désactivé "
                    )
                    return render(request, 'optionnelles/login.html', {'form': form})
            else:
                form.add_error(None,
                    "Les identifiants de connexion sont incorrectes "
                )
                return render(request, 'optionnelles/login.html', {'form': form})
                #form = ConnexionForm(request.POST)
                #return render(request, 'optionnelles/login.html', {'form': form})
    else:
        form = ConnexionForm()
        return render(request, 'optionnelles/login.html', {'form': form})

class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/options/login')

def user_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            djangoUser = User.objects.create_user(username=data['username'], email=data['email'],password=data['password'])
            my_group = Group.objects.get(name='Etudiant') 
            my_group.user_set.add(djangoUser)
            djangoUser.first_name = username=data['prenom']
            djangoUser.last_name = username=data['nom']
            djangoUser.is_active = "False"
            djangoUser.save()
            etudiantUser = Etudiant(numero_etudiant=data['numero_etudiant'],ajac=data['ajac'],redoublant=data['redoublant'],telephone=data['telephone'])
            etudiantUser.utilisateur = djangoUser
            etudiantUser.save()
            etudiantUser.parcours.add(data['parcours'])
            etudiantUser.save()

            return HttpResponseRedirect('/options/demande_inscription')
        else:
            form.add_error(None,
                    "L'inscription a échoué"
                    )
    else:
        form = InscriptionForm()
    return render(request, 'optionnelles/inscription.html', {'form': form})

def user_motDePasseOublie(request):
    if request.method == 'POST':
        form = MpoublieForm(request.POST)
        if form.is_valid(): #verifier que l'adresse mail est contenu dans la BDD
            return HttpResponseRedirect('/options/demande_reinitialisation') #rediriger vers la page de validation
        else:
            raise forms.ValidationError(
                    "L'adresse email n'est pas valide "
                    )
    else:
        form = MpoublieForm()
    return render(request, 'optionnelles/motDePasseOublie.html', {'form': form})

def user_formulaireReinitialisation(request):
    if request.method == 'POST':
        form = ReinitialisationForm(request.POST)
        if form.is_valid(): #verifier que l'adresse mail est contenu dans la BDD
            return HttpResponseRedirect('/options/validation_reinitialisation') #rediriger vers la page de validation
        else:
            raise forms.ValidationError(
                    "Le mot de passe n'est pas identique"
                    )
    else:
        form = ReinitialisationForm()
    return render(request, 'optionnelles/formulaire_reinitialisation.html', {'form': form})

def user_demandeReinitialisation(request):
    return render(request, 'optionnelles/validation_demande.html')

def user_demandeInscription(request):
    return render(request, 'optionnelles/demande_inscription.html')

def user_validationReinitialisation(request):
    return render(request, 'optionnelles/validation_reinitialisation.html')
# Create your views here.
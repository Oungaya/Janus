from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import Etudiant
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.template.context_processors import csrf
from .forms import ConnexionForm, InscriptionForm, MpoublieForm, ReinitialisationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .optionnellesHelpers import getGroupTemplate

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
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/validation_inscription_admin.html', context)

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
                    raise forms.ValidationError(
                    "Votre compte n'a pas encore été activé ou a été désactivé "
                    )
            else:
                raise forms.ValidationError(
                    "Les identifiants de connexion sont incorrectes "
                )
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
            return HttpResponseRedirect('/options/demande_inscription')
        else:
            raise forms.ValidationError(
                    "Votre compte n'a pas encore été activé ou a été désactivé "
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
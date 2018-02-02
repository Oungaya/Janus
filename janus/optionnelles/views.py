from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from .models import Etudiant
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.template.context_processors import csrf


def index(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'optionnelles/index.html', context)

def user_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'user': user,
    }
    return render(request, 'optionnelles/user.html', context)


class LoginView(TemplateView):
    template_name = 'optionnelles/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/options/')
            else:
                return HttpResponse('Mot de passe et/ou nom d\'utilisateur incorrect <a href="/options/login"">Se connecter</a>')
        else:
            return HttpResponse('Erreur : Champ nom d\'utilisateur et/ou mot de passe vide. <a href="/options/login">Se connecter</a>')

class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/options/login')

def user_inscription(request):
    return render(request, 'optionnelles/inscription.html')

def user_motDePasseOublie(request):
    return render(request, 'optionnelles/motDePasseOublie.html')

# Create your views here.
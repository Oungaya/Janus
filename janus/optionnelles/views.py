from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Etudiant
from django.contrib.auth.models import User

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

def user_connection(request):
    return render(request, 'optionnelles/login.html')

def user_inscription(request):
    return render(request, 'optionnelles/inscription.html')

def user_motDePasseOublie(request):
    return render(request, 'optionnelles/motDePasseOublie.html')

# Create your views here.
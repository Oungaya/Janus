from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:user_id>/user/', views.user_detail, name='user_detail'),
    path('login/', views.user_connection, name='user_connection'),
    path('inscription/', views.user_inscription, name='user_inscription'),
    path('oubli-mdp/', views.user_motDePasseOublie, name='user_motDePasseOublie')
]
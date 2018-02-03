from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:user_id>/user/', views.user_detail, name='user_detail'),
    path('login/', views.user_connection, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('inscription/', views.user_inscription, name='user_inscription'),
    path('oubli-mdp/', views.user_motDePasseOublie, name='user_motDePasseOublie'),
    path('demande_reinitialisation/', views.user_demandeReinitialisation, name='user_demandeReinitialisation'),
    path('demande_inscription/', views.user_demandeInscription, name='user_demandeInscription')
]
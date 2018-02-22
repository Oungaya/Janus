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
    path('demande_inscription/', views.user_demandeInscription, name='user_demandeInscription'),
    path('validation_reinitialisation/', views.user_validationReinitialisation, name='user_validationReinitialisation'),
    path('formulaire_reinitialisation/', views.user_formulaireReinitialisation, name='user_formulaireReinitialisation'),
    path('validation_inscription/', views.admin_ValidationInscription, name='admin_ValidationInscription'),
    path('inscription_professeur/', views.admin_InscriptionProfesseur, name='admin_InscriptionProfesseur'),
    path('validation_inscription/<int:num_etu>/user/', views.admin_ValidationInscriptionDetails, name='admin_ValidationInscriptionDetails'),
    path('validation_inscription/<int:num_etu>/end/', views.admin_ValidationInscriptionEnd, name='admin_ValidationInscriptionEnd')
]
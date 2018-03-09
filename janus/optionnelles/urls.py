from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='optionnelles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:user_id>/user/', views.user_detail, name='user_detail'),
    path('login/', views.user_connection, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('inscription/', views.user_inscription, name='user_inscription'),
    path('demande_reinitialisation/', views.user_demandeReinitialisation, name='user_demandeReinitialisation'),
    path('demande_inscription/', views.user_demandeInscription, name='user_demandeInscription'),
    path('validation_reinitialisation/', views.user_validationReinitialisation, name='user_validationReinitialisation'),
    path('formulaire_reinitialisation/', views.user_formulaireReinitialisation, name='user_formulaireReinitialisation'),
    path('validation_inscription/', views.admin_ValidationInscription, name='admin_ValidationInscription'),
    path('inscription_professeur/', views.admin_InscriptionProfesseur, name='admin_InscriptionProfesseur'),
    path('validation_inscription/<num_etu>/user/', views.admin_ValidationInscriptionDetails, name='admin_ValidationInscriptionDetails'),
    path('validation_inscription/<num_etu>/end/', views.admin_ValidationInscriptionEnd, name='admin_ValidationInscriptionEnd'),
    path('selection_groupe/<int:id_ue>/', views.admin_selectionGroupe, name='admin_selectionGroupe'),
    url(r'^ajax/change_groupe/$', views.change_groupe, name='change_groupe'),
    url(r'^ajax/notification_inscription/$', views.notification_inscription, name='notification_inscription'),
    path('choix_ue_groupe/', views.admin_choixUeGroupe, name='admin_choixUeGroupe'),
    #gestion du mot de passe oublié
    url(r'^password_reset/$', auth_views.password_reset,{'email_template_name':'optionnelles/registration/password_reset_email.html',
                                                    'template_name':'optionnelles/registration/password_reset_form.html',
                                                    'subject_template_name':'optionnelles/registration/password_reset_subject.txt',
                                                    'post_reset_redirect':'optionnelles:password_reset_done',
                                                    'from_email':'optionnelles@django.com',
                                                    },name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'optionnelles/registration/password_reset_done.html'}, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm,
                                                    {'template_name': 'optionnelles/registration/password_reset_confirm.html',
                                                    'post_reset_redirect': 'optionnelles:password_reset_complete'},
                                                    name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'optionnelles/registration/password_reset_complete.html'},name='password_reset_complete'),
]
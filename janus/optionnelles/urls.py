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
    path('oubli-mdp/', views.user_motDePasseOublie, name='user_motDePasseOublie'),
    path('demande_reinitialisation/', views.user_demandeReinitialisation, name='user_demandeReinitialisation'),
    path('demande_inscription/', views.user_demandeInscription, name='user_demandeInscription'),
    path('validation_reinitialisation/', views.user_validationReinitialisation, name='user_validationReinitialisation'),
    path('formulaire_reinitialisation/', views.user_formulaireReinitialisation, name='user_formulaireReinitialisation'),
    path('validation_inscription/', views.admin_ValidationInscription, name='admin_ValidationInscription'),
    path('inscription_professeur/', views.admin_InscriptionProfesseur, name='admin_InscriptionProfesseur'),
    path('validation_inscription/<num_etu>/user/', views.admin_ValidationInscriptionDetails, name='admin_ValidationInscriptionDetails'),
    path('validation_inscription/<num_etu>/end/', views.admin_ValidationInscriptionEnd, name='admin_ValidationInscriptionEnd'),
    #url(r'^password_reset/$', auth_views.password_reset, name='password_reset_form'),
    #url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    #url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    auth_views.password_reset_confirm, name='password_reset_confirm'),
    #url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #url('^', include('django.contrib.auth.urls')),
    #path('oubli-mdp/', auth_views.password_reset, name='user_motDePasseOublie'),
    #path('password_reset/done', auth_views.password_reset_done, name='registration/password_reset_done')
    #url(r'^password_reset/$', auth_views.password_reset, name='registration/password_reset_form.html'),
    #url(r'password_reset/done/', auth_views.password_reset_done, name='registration/password_reset_done'), 
    #url(r'password_reset/', auth_views.password_reset, name='registration/password_reset'),
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
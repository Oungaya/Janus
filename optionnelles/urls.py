from django.conf.urls import url, include
from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
#from optionnellesHelpers import NegativeIntConverter
class NegativeIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value


register_converter(NegativeIntConverter, 'negint')

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
    #path('liste_professeur/', views.admin_listeProfesseurs, name='admin_liste_professeur'),
    path('inscription_professeur/', views.admin_InscriptionProfesseur, name='admin_InscriptionProfesseur'),
    path('liste_professeur/', views.admin_ListeProfesseur, name='admin_ListeProfesseur'),
    path('modification_professeur/<int:id_prof>/user/', views.admin_ProfesseurDetails, name='admin_ProfesseurDetails'),
    path('modification_professeur/<int:id_prof>/end/', views.admin_ProfesseurEnd, name='admin_ProfesseurEnd'),
    path('validation_inscription/<num_etu>/user/', views.admin_ValidationInscriptionDetails, name='admin_ValidationInscriptionDetails'),
    path('validation_inscription/<num_etu>/end/', views.admin_ValidationInscriptionEnd, name='admin_ValidationInscriptionEnd'),
    url(r'^ajax/valide_ue/$', views.valide_ue, name='valide_ue'),
    path('inscription_admin/', views.admin_InscriptionAdmin, name='admin_InscriptionAdmin'),
    path('liste_admin/', views.admin_ListeAdmin, name='admin_ListeAdmin'),
    path('liste_periodes/', views.admin_ListePeriodes, name='admin_ListePeriodes'),
    path('ajout_periode/', views.admin_AjoutPeriode, name='admin_AjoutPeriode'),
    path('modification_periode/<int:id_periode>/user/', views.admin_PeriodeDetails, name='admin_PeriodeDetails'),
    path('modification_periode/<int:id_periode>/end/', views.admin_PeriodeEnd, name='admin_PeriodeEnd'),
    path('modification_admin/<int:id_admin>/user/', views.admin_AdminDetails, name='admin_AdminDetails'),
    path('modification_admin/<int:id_admin>/end/', views.admin_AdminEnd, name='admin_AdminEnd'),
    path('selection_groupe/<int:id_ue>/', views.admin_selectionGroupe, name='admin_selectionGroupe'),
    url(r'^ajax/change_groupe/$', views.change_groupe, name='change_groupe'),
    url(r'^ajax/choix_options/$', views.valider_choix_options, name='valider_choix_options'),
    url(r'^ajax/notification_inscription/$', views.notification_inscription, name='notification_inscription'),
    path('choix_ue_groupe/', views.admin_choixUeGroupe, name='admin_choixUeGroupe'),
    path('liste_emargement/', views.liste_emargement, name='liste_emargement'),
    path('emargement/<int:id_ue>/', views.emargement, name='emargement'),
    path('choix_options/', views.etudiant_choixOptions, name='choix_options'),
    path('export_csv/<int:id_ue>/<int:id_groupe>', views.exportCSV, name='export_csv'),
    path('export_pdf/<int:id_ue>/<int:id_groupe>', views.exportPDF, name='export_pdf'),
    path('export_csv_custom/<negint:id_ue>/<int:id_groupe>/<negint:id_pole>/<negint:id_parcours>/<negint:id_semestre>/<negint:id_promotion>/', views.exportCSV_emmargement, name='export_csv_custom'),
    path('export_pdf_custom/<negint:id_ue>/<int:id_groupe>/<negint:id_pole>/<negint:id_parcours>/<negint:id_semestre>/<negint:id_promotion>/', views.exportPDF_emmargement, name='export_pdf_custom'),
    path('mes_cours/', views.etudiant_mesCours, name='mes_cours'),
    url(r'^ajax/population_liste/$', views.population_liste, name='population_liste'),
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
    path('attribution_ue_index/', views.admin_attributionUe, name='attribution_ue_index'),
    path('ue_manquantes/', views.admin_uesManquantes, name='admin_uesManquantes'),
    ### URL temporaires 
    path('generateur_temp/', views.generateur_temp, name='generateur_temp'),
    path('aggreg_pref/', views.aggreg_pref, name='aggreg_pref')
]
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from .models import Etudiant, Professeur, Parcours, Statut, UE, Etudiant_par_UE, Pole_par_Semestre, Pole, Semestre, AnneeCourante, UE_par_Pole
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.template.context_processors import csrf
from django.template import loader, Context
from .forms import ConnexionForm, InscriptionForm, InscriptionProfesseurForm, MpoublieForm, ReinitialisationForm, ValidationUserByAdminForm, ModificationProfByAdminForm, InscriptionAdminForm, ModificationAdminForm, AjoutPeriodeForm, ModificationPeriodeForm
from django.contrib.auth.decorators import login_required
from django import forms
from .optionnellesHelpers import getGroupTemplate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.core.mail import send_mail
from .generateur import generate_etudiant, bulk_generate_etudiant, attribution_ue, testset001
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
import random, string, csv, json, codecs, io, tempfile
from weasyprint import HTML
from django.template.loader import render_to_string
#si USE_TZ = True
from django.utils import timezone
#si USE_TZ = False
import datetime


def generer_mdp():
    length = 8
    mdp = []
    mdp.append(random.choice(string.ascii_lowercase))
    mdp.append(random.choice(string.ascii_uppercase))
    mdp.append(str(random.randint(0,9)))
    random.shuffle(mdp)
    return ''.join(mdp)

@login_required
def exportCSV(request, id_ue, id_groupe):
    # Create the HttpResponse object with the appropriate CSV header.
    ue = UE.objects.get(pk=id_ue)
    
    #if id_groupe == 0:
    
    liste_etudiant = Etudiant.objects.filter(etudiant_par_ue__ue_id=ue.id).order_by("utilisateur__last_name")
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    csv.register_dialect('unixpwd', delimiter=';', quoting=csv.QUOTE_NONE)
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)

    writer.writerow(["Numéro étudiant; Nom; Prénom; Options;"])

    for e in liste_etudiant:
        string_ue = ""
        EtudiantParUE = Etudiant_par_UE.objects.filter(etudiant__id=e.id)
        for o in EtudiantParUE:
            if o.optionnelle == True and o.choisie == True:
                string_ue +=o.ue.nom + " : " + o.ue.code_apoge

        writer.writerow([e.numero_etudiant + ";" + e.utilisateur.last_name + ";" + e.utilisateur.first_name + ";" + string_ue + ";"])
        
    return response

@login_required
def exportPDF(request, id_ue, id_groupe):
    """
    ue = UE.objects.get(pk=id_ue)
    
    #if id_groupe == 0:
    
    liste_etudiant = Etudiant.objects.filter(etudiant_par_ue__ue_id=ue.id)
    liste_etudiant_nom = Etudiant.objects.values_list('utilisateur__first_name',flat=True)
    liste_etudiant_prenom = Etudiant.objects.values_list('utilisateur__last_name',flat=True)
    print(liste_etudiant)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="'+ ue.nom +' export.pdf"'

    buff = io.StringIO()
    elements = []
    cm = 2.54
    doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)

    data=[liste_etudiant_nom,liste_etudiant_prenom]
    print(liste_etudiant_nom)
    print(liste_etudiant_prenom)
    table = Table(data, colWidths=270, rowHeights=79)
    elements.append(table)
    doc.build(elements) 
    response.write(buff.getvalue())
    buff.close()
    """
    ue = UE.objects.get(pk=id_ue)
    liste_etudiant = Etudiant.objects.filter(etudiant_par_ue__ue_id=ue.id, etudiant_par_ue__choisie=True).order_by("utilisateur__last_name")
    groupe = id_groupe
    if id_groupe == 0:
        groupe = "Promotion complète"


    # Rendered
    html_string = render_to_string('export/export_pdf.html', {'liste_etudiant': liste_etudiant, 'ue': ue, 'groupe' : groupe})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'attachment; filename="'+ ue.nom +' export.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response

@login_required
def index(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/index.html', context)

@login_required
def admin_choixUeGroupe(request):
    liste_ue = UE.objects.all()
    context = {
        'liste_ue': liste_ue,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/choix_ue_groupe.html', context)

@login_required
def emargement(request, id_ue):
    nom_ue = UE.objects.get(pk=id_ue)
    liste_etudiant = Etudiant.objects.filter(etudiant_par_ue__ue__id=id_ue,etudiant_par_ue__choisie=True).order_by("utilisateur__last_name")

    context = {
        'liste_etudiant': liste_etudiant,
        'ue': id_ue,
        'nom_ue': nom_ue,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/emargement.html', context)

@login_required
def liste_emargement(request):
    auth = request.user.is_staff
    liste_ue = UE.objects.all()


    context = {
        'liste_ue': liste_ue,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/emargement_liste_ue.html', context)


@login_required
def admin_selectionGroupe(request, id_ue):
    ue = UE.objects.get(pk=id_ue)
    user_list = Etudiant.objects.filter(utilisateur__is_active=True, ues__id=id_ue).order_by("utilisateur__last_name")
    if ue.nombre_groupes != 0:
        col = int(12/ue.nombre_groupes)
    else:
        col = 0
    context = {
        'user_list': user_list,
        'ue': ue,
        'range': range(ue.nombre_groupes),
        'col': col,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/selection_groupe.html', context)

def change_groupe(request):
    etudiant_id = request.GET.get('etudiant', None)
    ue_id = request.GET.get('ue', None)
    groupe = request.GET.get('groupe', None)

    #set les groupes aux etudiants 
    e = Etudiant.objects.get(pk=etudiant_id)
    ue = UE.objects.get(pk=ue_id)

    EtudiantParUE = Etudiant_par_UE.objects.get(etudiant__id=e.id,ue__id=ue.id)
    EtudiantParUE.groupe = groupe
    EtudiantParUE.save()

    data = {
        'is_taken': 1
    }
    return JsonResponse(data)

def valide_ue(request):
    ue_id = request.GET.get('ue', None)
    etudiant = request.GET.get('etudiant', None)
    ue = UE.objects.get(pk=ue_id)
    #Récup l'étudiant pour vérifier s'il est redoublant
    '''e = Etudiant.objects.get(pk=etudiant)
    print(e)
    if(e.redoublant == False):
        e.redoublant = not e.redoublant
    else:
        e.redoublant = not e.redoublant
    e.save()'''
    EtudiantParUE = Etudiant_par_UE.objects.get(etudiant__id=etudiant,ue__id=ue.id)
    EtudiantParUE.valide = not EtudiantParUE.valide
    EtudiantParUE.save()
    
    print(e.redoublant)
    data = {
        'is_valid': 1,
        #'is_redoublant': e.redoublant
    }
    return JsonResponse(data)

def notification_inscription(request):

    nombre_inscription = Etudiant.objects.filter(utilisateur__is_active=False).count()

    data = {
        'nombre_notification': nombre_inscription
    }
    return JsonResponse(data)

def valider_choix_options(request):
    etudiant = Etudiant.objects.get(utilisateur=request.user.id)
    liste_choix = json.loads(request.GET.get('dict'))
    flag = True
    #print(liste_choix)
    for ue in liste_choix:
        if Etudiant_par_UE.objects.filter(etudiant__id=etudiant.id, ue__id=ue['ue']).exists():
            print(ue['ue']) 
        else:
            flag = False

    if flag == True:
        for ue in liste_choix:
            EtudiantParUE = Etudiant_par_UE.objects.get(etudiant__id=etudiant.id,ue__id=ue['ue'])
            EtudiantParUE.order = ue['ordre']
            EtudiantParUE.save()
        data = {
            'error': 0
        }
    else:
        data = {
            'error': 1
        }
    return JsonResponse(data)


@login_required
def admin_ValidationInscription(request):
    liste_etudiant = Etudiant.objects.filter(utilisateur__is_active=False).order_by("utilisateur__last_name")
    context = {
        'liste_etudiant': liste_etudiant,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/validation_inscription_admin.html', context)

@login_required
def admin_listeProfesseurs(request):
    liste_professeur = Professeur.objects.filter(utilisateur__is_active=True).order_by("utilisateur__last_name")
    context = {
        'liste_professeur': liste_professeur,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/admin_liste_professeur.html', context)

@login_required
def etudiant_choixOptions(request):
    etudiant = Etudiant.objects.get(utilisateur=request.user.id)
    parcours_etudiant = etudiant.parcours.first()
    #date_debut_options = AnneeCourante.objects.get(parcours=parcours_etudiant)
    #date_fin_options = AnneeCourante.objects.get(parcours=parcours_etudiant)
    poles_parcours = Pole.objects.filter(parcours=parcours_etudiant).all()
    res = {}
    if AnneeCourante.objects.filter(parcours=parcours_etudiant).exists():
        has_period = True
        #utc=pytz.UTC
        date_debut_options1 = AnneeCourante.objects.get(parcours=parcours_etudiant).date_debut_options1
        date_fin_options1 = AnneeCourante.objects.get(parcours=parcours_etudiant).date_fin_options1
        date_debut_options2 = AnneeCourante.objects.get(parcours=parcours_etudiant).date_debut_options2
        date_fin_options2 = AnneeCourante.objects.get(parcours=parcours_etudiant).date_fin_options2
        '''date_debut_options1 = utc.localize(date_debut_options1)
        date_fin_options1 = utc.localize(date_fin_options1)
        date_debut_options2 = utc.localize(date_debut_options2)
        date_fin_options2 = utc.localize(date_fin_options2)'''

        #now = timezone.now()

        #print(now)

        '''if(datetime.now() >= date_debut_options1 and datetime.now() <= date_fin_options1):
            print("on est en S1")
        elif(datetime.now() >= date_debut_options2 and datetime.now() <= date_fin_options2):
            print("on est en S2")'''

        now = datetime.datetime.now()
        
        dateFinOptions = ""
        if(now >= date_debut_options1 and now <= date_fin_options1):    
            for pole in poles_parcours:
                liste_ues = etudiant.ues.filter(etudiant_par_ue__optionnelle=True, poles=pole.id, semestre_id=1).order_by('etudiant_par_ue__order')
                res[pole] = liste_ues
                dateFinOptions = date_fin_options1
                #print(liste_ues)
        elif(now >= date_debut_options2 and now <= date_fin_options2):
            for pole in poles_parcours:
                liste_ues = etudiant.ues.filter(etudiant_par_ue__optionnelle=True, poles=pole.id, semestre_id=2).order_by('etudiant_par_ue__order')
                res[pole] = liste_ues
                dateFinOptions = date_fin_options2
                #print(liste_ues)
    else:
        has_period = False
        dateFinOptions = None
    context = {
        'res': res,
        'template_group': getGroupTemplate(request.user),
        'dateFinOptions': dateFinOptions,
        'has_period' : has_period
    }
    return render(request, 'optionnelles/etudiant_choix_options.html', context)

@login_required
def etudiant_mesCours(request):
    etudiant = Etudiant.objects.get(utilisateur=request.user.id)
    parcours_id_etudiant = etudiant.parcours.first().id
    parcours_etudiant = etudiant.parcours.first()
    poles_parcours = Pole.objects.filter(parcours=parcours_etudiant).all()
    res = {}
    for pole in poles_parcours:
        res[pole] = {}
        semestres_par_pole = Pole_par_Semestre.objects.filter(pole=pole.id).all()
        for semestre in semestres_par_pole:
            liste_ues_valide_option = etudiant.ues.filter(etudiant_par_ue__optionnelle=True, etudiant_par_ue__choisie=True, semestre_id=semestre.semestre_id, poles=pole.id)
            liste_ues_valide_oblig = etudiant.ues.filter(etudiant_par_ue__optionnelle=False, etudiant_par_ue__choisie=True, semestre_id=semestre.semestre_id, poles=pole.id)
            res[pole][semestre] = {'UE obligatoire(s)': liste_ues_valide_oblig, 'UE optionnelle(s)': liste_ues_valide_option}
    context = {
        'res':res,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/etudiant_mes_cours.html', context)

@login_required
def admin_ValidationInscriptionDetails(request, num_etu):
    etu = Etudiant.objects.get(numero_etudiant = num_etu)
    form = ValidationUserByAdminForm(initial={
        'nom': etu.utilisateur.last_name,
        'prenom': etu.utilisateur.first_name,
        'numero_etudiant': etu.numero_etudiant,
        'telephone': etu.telephone,
        'parcours': etu.parcours.first(),
        'ajac': etu.ajac,
        'redoublant': etu.redoublant,
        'email': etu.utilisateur.email
        })
    context = {
        'etudiant': etu,
        'template_group': getGroupTemplate(request.user),
        'form' : form
    }
    return render(request, 'optionnelles/validation_inscription_admin_detail.html', context)

@login_required
def admin_ValidationInscriptionEnd(request, num_etu):
    etu = Etudiant.objects.get(numero_etudiant = num_etu)
    if request.method == 'POST':
        form = ValidationUserByAdminForm(request.POST)
        if request.POST.get("accept"):
            if form.is_valid():
                data = form.cleaned_data
                if etu.numero_etudiant != data['numero_etudiant']:
                    etu.numero_etudiant = data['numero_etudiant']
                if etu.ajac != data['ajac']:
                    etu.ajac = data['ajac']
                if etu.redoublant != data['redoublant']:
                    etu.redoublant = data['redoublant']
                if etu.parcours != data['parcours']:
                    etu.parcours.clear()
                    etu.parcours.add(data['parcours'])
                        
                if etu.telephone != data['telephone']:
                    etu.telephone = data['telephone']
            
                etu.save()

                etu.utilisateur.first_name = data['prenom']
                etu.utilisateur.last_name = data['nom']
                etu.utilisateur.email = data['email']
                etu.utilisateur.is_active = True
                etu.utilisateur.save()

                messages.success(request, 'Utilisateur validé')
                return HttpResponseRedirect('/options/validation_inscription/')
            else:
                return HttpResponseRedirect('/options/validation_inscription/') 
        #fmy - on ne fais rien en cas de refus (remarques client WP3)
        #else:
            #Etudiant.objects.get(numero_etudiant = num_etu).delete()
        return HttpResponseRedirect('/options/validation_inscription/') 
    

@login_required
def admin_InscriptionProfesseur(request):
    user_list = User.objects.all()
    professeur_list = Professeur.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }

    if request.method == 'POST':
        form = InscriptionProfesseurForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            password = generer_mdp()
            djangoUser = User.objects.create_user(username=data['prenom'][0].lower()+data['nom'].lower(), email=data['email'], password=password)
            my_group = Group.objects.get(name='Professeur') 
            my_group.user_set.add(djangoUser)
            djangoUser.first_name = username=data['prenom']
            djangoUser.last_name = username=data['nom']
            djangoUser.is_active = "True"
            djangoUser.save()
            professeurUser = Professeur( statut=data['statut'])
            professeurUser.utilisateur = djangoUser
            #professeurUser.statut.add(data['statut'])
            professeurUser.save()
            if data['notifierParMail'] :
                send_mail(
                    'Inscription plateforme de gestion des feuilles d\'émargement - Janus',
                    'Bonjour,\n Vous avez été inscrit sur Janus, pour accéder à votre compte veuillez utiliser les '\
                    'identifiants suivant : \n\t nom d\'utilisateur : ' + djangoUser.username + ' \n\t mot de pase : ' + password
                    + ' \n\n Cordialement,\n\n l\'équipe Janus.',
                    'from@example.com',
                    [djangoUser.email],
                    fail_silently=False)
            messages.success(request, 'Le professeur a été ajouté')
            return HttpResponseRedirect('/options/liste_professeur')
        else:
            form.add_error(None,
                "L'inscription a échoué"
                )
    else:
        form = InscriptionProfesseurForm()

    return render(request, 'optionnelles/inscription_professeur_admin.html', {'form': form,'user_list': user_list,'template_group': getGroupTemplate(request.user)})

@login_required
def admin_InscriptionAdmin(request):
    liste_admin = User.objects.filter(is_staff=True)    
    context = {
        'liste_admin': liste_admin,
        'template_group': getGroupTemplate(request.user)
    }

    if request.method == 'POST':
        form = InscriptionAdminForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            djangoUser = User.objects.create_user(username=data['prenom'][0].lower()+data['nom'].lower(), email=data['email'], password=generer_mdp())
            djangoUser.first_name = username=data['prenom']
            djangoUser.last_name = username=data['nom']
            djangoUser.is_staff = "True"
            djangoUser.save()

            messages.success(request, 'L\'administrateur a été ajouté')
            return HttpResponseRedirect('/options/liste_admin')
        else:
            form.add_error(None,
                "L'inscription a échoué"
                )
    else:
        form = InscriptionAdminForm()

    return render(request, 'optionnelles/inscription_admin.html', {'form': form,'liste_admin': liste_admin,'template_group': getGroupTemplate(request.user)})

@login_required
def admin_ListeProfesseur(request):
    liste_professeur = Professeur.objects.all
    context = {
        'liste_professeur': liste_professeur,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/professeur_liste_admin.html', context)

@login_required
def admin_ListeAdmin(request):
    liste_admin = User.objects.filter(is_staff=True)
    context = {
        'liste_admin': liste_admin,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/liste_admin.html', context)

@login_required
def admin_ListePeriodes(request):
    liste_periodes = AnneeCourante.objects.all
    context = {
        'liste_periodes': liste_periodes,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/liste_periodes.html', context)

@login_required
def admin_PeriodeDetails(request, id_periode):
    periode = AnneeCourante.objects.get(pk=id_periode)
    form = ModificationPeriodeForm(initial={
        'nom': periode.nom,
        'parcours': periode.parcours,
        'dateDebutS1': periode.date_debut_semestre1,
        'dateDebutS2': periode.date_debut_semestre2,
        'dateFinS1': periode.date_fin_semestre1,
        'dateFinS2': periode.date_fin_semestre2,
        'dateDebutOptionsS1': periode.date_debut_options1,
        'dateDebutOptionsS2': periode.date_debut_options2,
        'dateFinOptionsS1': periode.date_fin_options1,
        'dateFinOptionsS2': periode.date_fin_options2,
        'date_debut_annee': periode.date_debut_annee,
        'date_fin_annee': periode.date_fin_annee
    })
    context = {
        'periode': periode,
        'template_group': getGroupTemplate(request.user),
        'form' : form
    }
    return render(request, 'optionnelles/periode_details.html', context)

@login_required
def admin_PeriodeEnd(request, id_periode):
    periode = AnneeCourante.objects.get(pk=id_periode)
    if request.method == 'POST':
        form = ModificationPeriodeForm(request.POST)
        if request.POST.get("modif"):
            if form.is_valid():
                data = form.cleaned_data
                periode.nom = data['nom']
                periode.parcours = data['parcours']
                periode.date_debut_semestre1 = data['dateDebutS1']
                periode.date_debut_semestre2 = data['dateDebutS2']
                periode.date_fin_semestre1 = data['dateFinS1']
                periode.date_fin_semestre2 = data['dateFinS2']
                periode.date_debut_options1 = data['dateDebutOptionsS1']
                periode.date_debut_options2 = data['dateDebutOptionsS2']
                periode.date_fin_options1 = data['dateFinOptionsS1']
                periode.date_fin_options2 = data['dateFinOptionsS2']
                periode.date_debut_annee = data['date_debut_annee']
                periode.date_fin_annee = data['date_fin_annee']
                periode.save()
                messages.success(request, 'Periode modifiée')
                return HttpResponseRedirect('/options/liste_periodes/')
            else:
                form.add_error(None, "La modification a échoué")
        else:
            return HttpResponseRedirect('/options/liste_periodes/')

@login_required
def admin_AjoutPeriode(request):
    if request.method == 'POST':
        form = AjoutPeriodeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            periode = AnneeCourante(nom=data['nom'], parcours=data['parcours'], date_debut_semestre1=data['dateDebutS1'], date_debut_semestre2=data['dateDebutS2'], date_fin_semestre1=data['dateFinS1'], date_fin_semestre2=data['dateFinS2'], date_debut_options1=data['dateDebutOptionsS1'], date_debut_options2=data['dateDebutOptionsS2'], date_fin_options1=data['dateFinOptionsS1'], date_fin_options2=data['dateFinOptionsS2'], date_debut_annee=['date_debut_annee'], date_fin_annee=['date_fin_annee'])
            periode.save()
            messages.success(request, 'La période a été crée')
            return HttpResponseRedirect('/options/liste_periodes')
        else:
            form.add_error(None, "La création a échoué")
    else:
        form = AjoutPeriodeForm()
    return render(request, 'optionnelles/ajout_periode.html', {'form': form, 'template_group': getGroupTemplate(request.user)})

@login_required
def admin_AdminDetails(request, id_admin):
    admin = User.objects.filter(is_staff=True).get(pk=id_admin)
    form = ModificationAdminForm(initial={
        'nom': admin.last_name,
        'prenom': admin.first_name,
        'username': admin.username,
        #'groupe': admin.groupe.first(),
        'email': admin.email
        })
    context = {
        'administrateur': admin,
        'template_group': getGroupTemplate(request.user),
        'form' : form
    }
    return render(request, 'optionnelles/admin_details.html', context)

@login_required
def admin_AdminEnd(request, id_admin):
    admin = User.objects.filter(is_staff=True).get(pk=id_admin)
    if request.method == 'POST':
        form = ModificationAdminForm(request.POST)
        if request.POST.get("modif"):
            if form.is_valid():
                data = form.cleaned_data
                #if admin.groupe != data['groupe']:
                #    admin.groupe.through.objects.all().delete()
                #    admin.groupe.add(data['groupe'])
                #admin.save()

                admin.email = data['email']
                admin.username = data['username']
                admin.first_name = data['prenom']                                        
                admin.last_name = data['nom']
                admin.save()

                messages.success(request, 'Admin modifié')
                return HttpResponseRedirect('/options/liste_admin/')
            else:
                form.add_error(None,"La modification a échoué")
        else:
            return HttpResponseRedirect('/options/liste_admin/')

@login_required
def admin_ProfesseurDetails(request, id_prof):
    prof = Professeur.objects.get(pk=id_prof)
    form = ModificationProfByAdminForm(initial={
        'nom': prof.utilisateur.last_name,
        'prenom': prof.utilisateur.first_name,
        'username': prof.utilisateur.username,
        'statut': prof.statut,
        'email': prof.utilisateur.email
        })
    context = {
        'professeur': prof,
        'template_group': getGroupTemplate(request.user),
        'form' : form
    }
    return render(request, 'optionnelles/professeur_admin_details.html', context)

@login_required
def admin_ProfesseurEnd(request, id_prof):
    prof = Professeur.objects.get(pk=id_prof)
    if request.method == 'POST':
        form = ModificationProfByAdminForm(request.POST)
        if request.POST.get("modif"):
            if form.is_valid():
                data = form.cleaned_data
                if prof.statut != data['statut']:
                    prof.statut = data['statut']
                prof.save()

                prof.utilisateur.email = data['email']
                prof.utilisateur.username = data['username']
                prof.utilisateur.first_name = data['prenom']                                        
                prof.utilisateur.last_name = data['nom']
                prof.utilisateur.save()

                messages.success(request, 'Professeur modifié')
                return HttpResponseRedirect('/options/liste_professeur/')
            else:
                form.add_error(None,"La modification a échoué")
        else:
            return HttpResponseRedirect('/options/liste_professeur/')
        


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
            # ajac enlevé MAJ du 13/03/2018
            etudiantUser = Etudiant(numero_etudiant=data['numero_etudiant'],redoublant=data['redoublant'],telephone=data['telephone'])
            etudiantUser.utilisateur = djangoUser
            etudiantUser.save()
            etudiantUser.parcours.add(data['parcours'])
            #Affectation des UEs à l'étudiant en fontion de son parcours
            for k in etudiantUser.parcours.all():
                for i in k.pole_set.all():
                    for y in i.ue_par_pole_set.all():
                        ueEtudiant = Etudiant_par_UE(etudiant = etudiantUser, ue = y.ue, optionnelle = y.option, pole_ref = i.id)
                        if y.option==False:
                            ueEtudiant.choisie = True
                        ueEtudiant.save()
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

def generateur_temp(request):
    user_list = User.objects.all()
    bulk_generate_etudiant(100)
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user)
    }
    return render(request, 'optionnelles/generateur_temp.html', context)

def aggreg_pref(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
        'template_group': getGroupTemplate(request.user),
        'res' : attribution_ue()
    }
    return render(request, 'optionnelles/generateur_temp.html', context)
# Create your views here.
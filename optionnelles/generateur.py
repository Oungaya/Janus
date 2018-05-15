from .models import Etudiant, Professeur, Parcours, Statut, UE, Etudiant_par_UE, UE_par_Pole
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import random
import string


def generate_etudiant(_username,_email,_password,_prenom,_nom,_numetu,_ajac,_redoub,_tel,_parcours):
    ##### creation de l'étudiant 
    djangoUser = User.objects.create_user(username=_username, email=_email,password=_password)
    my_group = Group.objects.get(name='Etudiant') 
    my_group.user_set.add(djangoUser)
    djangoUser.first_name = _prenom
    djangoUser.last_name = _nom
    djangoUser.is_active = "True"
    djangoUser.save()
    # ajac enlevé MAJ du 13/03/2018
    etu = Etudiant(numero_etudiant=_numetu,redoublant=_redoub,telephone=_tel)
    etu.utilisateur = djangoUser
    etu.save()
    etu.parcours.add(_parcours)
    #Affectation des UEs à l'étudiant en fontion de son parcours
    for k in etu.parcours.all():#pour tous les parcours de l'étudiant
        for i in k.pole_set.all():# pour tous les poles (bloc) du parcours
            list_ue_etu = [] # stock les EtudiantParUe de ce pole
            for y in i.ue_par_pole_set.all():#pour toutes les ues de ce pole
                ue_etu = Etudiant_par_UE(etudiant = etu, ue = y.ue, optionnelle = y.option)
                if y.option:
                    list_ue_etu.append(ue_etu)
                else:
                    ue_etu.choisie = True
                    y.ue.capacite -= 1
                    y.ue.save()
                ue_etu.save()

            if y.option:
                random.shuffle(list_ue_etu)#met la liste des ue_etu dans un ordre random qui sera l'odre de préférence de l'étudiant
                for i in range(len(list_ue_etu)):
                    list_ue_etu[i].order = i
                    list_ue_etu[i].save()
    etu.save()

def bulk_generate_etudiant(number):
    num_etu = 10000500
    nb_parcours = Parcours.objects.all().count()
    res = []
    for _ in range(number):
        num_etu += 1
        str_num_etu = str(num_etu)
        intial = ''.join(random.choices(string.ascii_lowercase))
        generate_etudiant(
            intial+str_num_etu,
            intial+str_num_etu+"@u-picadie.fr",
            "kappa123",
            ''.join(random.choices(string.ascii_uppercase)) + ''.join(random.choices(string.ascii_lowercase, k = 5)),
            intial.upper()+''.join(random.choices(string.ascii_lowercase, k = 5)),
            str_num_etu,
            False,
            False,
            "0000000000",
            Parcours.objects.all()[random.randint(0,nb_parcours-1)])
        res.append(intial+str_num_etu)
    return res


def attribution_ue():
    choix_restant ={}
    debug_ue = {}
    # keep track of the ue each student still has to get
    for etu in Etudiant.objects.all():
        choix_restant[etu.id] = {}
        #print("etudiant" + str(etu.id))
        for par in etu.parcours.all():
            for pole in par.pole_set.all():
                #print(str(pole.id))
                choix_restant[etu.id][pole.id] = pole.a_choisir_dans_pole
    
    # première phase de la répartition : met les étudiants dans des ues autant que possible
    # des étudiants peuvent ne pas avoir assez d'ues dans certains poles à l'issue de cette étape
    for pref_ind in range(5):
        list_ue_etu = Etudiant_par_UE.objects.filter(order=pref_ind,choisie=False)
        for ue_etu in list_ue_etu:
            if ue_etu.ue.capacite > 0:
                for item in ue_etu.ue.ue_par_pole_set.all():
                    if item.pole.id in choix_restant[ue_etu.etudiant.id]:
                        key = item.pole.id
                if choix_restant[ue_etu.etudiant.id][key] > 0:
                    ue_etu.choisie = True
                    ue_etu.ue.capacite -= 1
                    choix_restant[ue_etu.etudiant.id][key] -= 1
                    ue_etu.save()
                    ue_etu.ue.save()
                    if ue_etu.ue.nom not in debug_ue:
                        debug_ue[ue_etu.ue.nom] = []
                    debug_ue[ue_etu.ue.nom].append(str(ue_etu.etudiant.utilisateur))
                    print(ue_etu.ue.nom + "  " + str(ue_etu.etudiant.utilisateur))
    
    # seconde phase de la répartition : crée des place dans des poles pour les étudiants au nombre
    # d'ues par pole pas suffisant (plus de place dans les ues lors de la première phase)
    """
    for etu_id, liste_pole in choix_restant.items():
        for pole_id, reste in liste_pole.items():
            while reste > 0:
                #prend la place d'un autre étudiant dans une ue de ce pole
    """

    return debug_ue
    

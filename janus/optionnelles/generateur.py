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
    for k in etu.parcours.all():
        for i in k.pole_set.all():
            list_ue_etu = [] # stock les EtudiantParUe de ce pole
            for y in i.ue_par_pole_set.all():
                ueEtudiant = Etudiant_par_UE(etudiant = etu, ue = y.ue, optionnelle = y.option)
                list_ue_etu.append(ueEtudiant)
                ueEtudiant.save()
            random.shuffle(list_ue_etu)#met la liste des ue_etu dans un ordre random qui sera l'odre de préférence de l'étudiant
            for i in range(len(list_ue_etu)):
                list_ue_etu[i].order = i
                list_ue_etu[i].save()
    etu.save()

def bulk_generate_etudiant(number,starting_num_etu):
    num_etu = starting_num_etu
    nb_parcours = Parcours.objects.all().count()
    for _ in range(number):
        num_etu += 1
        str_num_etu = str(num_etu)
        str_num_etu = str_num_etu.zfill(8-len(str_num_etu))
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

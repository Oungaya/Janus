from .models import Etudiant, Professeur, Parcours, Statut, UE, Etudiant_par_UE, UE_par_Pole
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
import random
import string
import sys
from django.core.management import call_command

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
                ue_etu = Etudiant_par_UE(etudiant = etu, ue = y.ue, optionnelle = y.option, pole_ref = i.id)
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
    num_etu = 10000000
    nb_parcours = Parcours.objects.all().count()
    res = []
    for _ in range(number):
        num_etu += 1
        str_num_etu = str(num_etu)
        intial = ''.join(random.choices(string.ascii_lowercase))
        User.objects.filter(username = intial+str_num_etu).delete()
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


def testset001():
    User.objects.filter(username = "a10000001").delete()
    generate_etudiant(
        "a10000001",
        "a10000001@u-picadie.fr",
        "kappa123",
        "prenom",
        "a",
        "10000001",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[2])
    User.objects.filter(username = "b10000002").delete()
    generate_etudiant(
        "b10000002",
        "b10000002@u-picadie.fr",
        "kappa123",
        "prenom",
        "b",
        "10000002",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[2])
    User.objects.filter(username = "c10000003").delete()
    generate_etudiant(
        "c10000003",
        "c10000003@u-picadie.fr",
        "kappa123",
        "prenom",
        "c",
        "10000003",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[5])
    User.objects.filter(username = "d10000004").delete()
    generate_etudiant(
        "d10000004",
        "d10000004@u-picadie.fr",
        "kappa123",
        "prenom",
        "d",
        "10000004",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[5])
    User.objects.filter(username = "e10000005").delete()
    generate_etudiant(
        "e10000005",
        "e10000005@u-picadie.fr",
        "kappa123",
        "prenom",
        "e",
        "10000005",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[6])
    User.objects.filter(username = "f10000006").delete()
    generate_etudiant(
        "f10000006",
        "f10000006@u-picadie.fr",
        "kappa123",
        "prenom",
        "f",
        "10000006",
        False,
        False,
        "0000000000",
        Parcours.objects.all()[6])


def attribution_ue():

    """ seems good, doesn't work : fixture are depreciated
    # save current database, for reasons ;)
    sysout = sys.stdout
    sys.stdout = open('db.xml', 'w')
    call_command('dumpdata','--exclude=contenttypes', '--exclude=auth.Permission')
    sys.stdout = sysout
    # get the data back with the command "python3.6 manage.py loaddata db.json" in the terminal
    """
    infos = {}
    # stock des infos pour faire l'attribution
    for etu in Etudiant.objects.all():
        infos[etu.id] = {}
        for par in etu.parcours.all():
            for pole in par.pole_set.all():
                if pole.a_choisir_dans_pole > 0:
                    infos[etu.id][pole.id] = {}
                    infos[etu.id][pole.id]["choix_restant"] = pole.a_choisir_dans_pole
                    infos[etu.id][pole.id]["ue_dispo"] = []

    potential_ue_etu = Etudiant_par_UE.objects.filter(choisie=False)
    for ue_etu in potential_ue_etu:
        if ue_etu.ue.capacite > 0:
            infos[ue_etu.etudiant.id][ue_etu.pole_ref]["ue_dispo"].append(ue_etu.ue.id)


    # première phase de la répartition : met les étudiants dans des ues autant que possible
    for pref_ind in range(30):
        list_ue_etu = Etudiant_par_UE.objects.filter(order=pref_ind,choisie=False)
        for ue_etu in list_ue_etu:
            if infos[ue_etu.etudiant.id][ue_etu.pole_ref]["choix_restant"] > 0:
                #si l'étudiant a encore des choix à faire
                if ue_etu.ue.capacite > 0:
                    #si l'ue n'est pas pleine
                    ue_etu.choisie = True
                    ue_etu.ue.capacite -= 1
                    infos[ue_etu.etudiant.id][ue_etu.pole_ref]["choix_restant"] -= 1
                    infos[ue_etu.etudiant.id][ue_etu.pole_ref]["ue_dispo"].remove(ue_etu.ue.id)
                    ue_etu.save()
                    ue_etu.ue.save()
                else:
                    # cette ue est pleine
                    print("denied [etu]" + str(ue_etu.etudiant.id).zfill(3) + " [ue]" + str(ue_etu.ue.id).zfill(3) + " [pole]" + str(ue_etu.pole_ref).zfill(3))
            else:
                pass
                # pas de pb : l'étudiant n'avait juste plus de choix à faire
                #print("l'étudiant " + str(ue_etu.etudiant.id) + " n'a plus d'ues à pourvoir dans le pole " + str(ue_etu.pole_ref))
    for _etudiant, _poles in infos.items():
        for p in _poles:
            if infos[_etudiant][p]["choix_restant"] > 0 :
                choix_restant_init = infos[_etudiant][p]["choix_restant"]
                while infos[_etudiant][p]["choix_restant"] > 0:
                    # tant que cet étudiant n'a pas toutes ses ues et qu'on a une chance de trouver une place
                    swapped = False
                    # pour toutes les ues non choisies de l'etudiant
                    for u in infos[_etudiant][p]["ue_dispo"]:
                        # cherche un étudiant qui a l'option et qui a d'autres options encore dispo
                        # liste des ue_etu potentiellement changeable
                        target_ue_etu = Etudiant_par_UE.objects.filter(ue=u,choisie=True,optionnelle=True)
                        for t in target_ue_etu:
                            if infos[t.etudiant.id][t.pole_ref]["choix_restant"] > 0:
                                # si l'autre etudiant est aussi en manque d'ues choisies
                                break
                            for UeId in infos[t.etudiant.id][t.pole_ref]["ue_dispo"]:
                                # parcours des ues du pole de l'étudiant qui perd sa place
                                if UE.objects.get(id = UeId).capacite > 0:
                                    print("SWAP")
                                    # transferts
                                    swapped = True
                                    # l'etudiant perdant sa place récupère l'autre ue (UeId)
                                    t.choisie = False
                                    new_ue_etu = Etudiant_par_UE.objects.get(ue=UeId,etudiant=t.etudiant.id)
                                    new_ue_etu.choisie = True
                                    infos[t.etudiant.id][t.pole_ref]["ue_dispo"].remove(UeId)
                                    infos[t.etudiant.id][t.pole_ref]["ue_dispo"].append(u)
                                    new_ue_etu.ue.capacite -= 1
                                    t.save()
                                    new_ue_etu.save()
                                    new_ue_etu.ue.save()
                                    # l'étudiant au pole non satisfait récupère la place dans l'ue (u)
                                    new_ue_etu = Etudiant_par_UE.objects.get(ue=u,etudiant=_etudiant)
                                    new_ue_etu.choisie = True
                                    infos[_etudiant][p]["ue_dispo"].remove(u)
                                    infos[_etudiant][p]["choix_restant"] -= 1
                                    new_ue_etu.save()
                                    break
                            if swapped:
                                break
                    if not swapped:
                        break
                print("[etu]" + str(_etudiant).zfill(3) + " [pole]" + str(p).zfill(3) + " [choix_restants] " + str(choix_restant_init) + " -> " + str(infos[_etudiant][p]["choix_restant"]))
                                
                            
                    


                              
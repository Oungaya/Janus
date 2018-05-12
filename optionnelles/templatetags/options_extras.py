from django import template
from ..models import Etudiant, Etudiant_par_UE
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='get_UE')
def get_UE(e, args):
    id_ue = int(args)
    return Etudiant_par_UE.objects.filter(etudiant__id=e.id,ue__id=id_ue)

@register.filter(name='has_no_group')
def has_group(UE, args):
    num_groupe = int(args)
    return UE.filter(groupe=num_groupe).exists()

@register.filter(name='has_group')
def has_group(UE, args):
    num_groupe = int(args) + 1
    return UE.filter(groupe=num_groupe).exists()

@register.filter(name='is_group') 
def is_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all() 

@register.filter(name='get_UE_valid')
def get_UE_valid(e, args):
    id_ue = int(args)
    e_par_ue = Etudiant_par_UE.objects.filter(etudiant__id=e.id,ue__id=id_ue)
    return e_par_ue.first().valide
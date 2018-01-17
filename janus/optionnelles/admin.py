
from django.contrib import admin
from .models import Professeur,Statut,Semestre,TypePole,Promotion,AnneeCourante,Parcours,Etudiant,Pole,UE,Etudiant_par_UE
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Statut)
admin.site.register(Professeur)
admin.site.register(Semestre)
admin.site.register(TypePole)
admin.site.register(Promotion)
admin.site.register(AnneeCourante)
admin.site.register(Parcours)
#admin.site.register(Etudiant)
admin.site.register(Pole)
admin.site.register(UE)

class UEInline(admin.TabularInline):
    model = Etudiant_par_UE
    extra = 2 # how many rows to show

class EtudiantAdmin(admin.ModelAdmin):
    inlines = (UEInline,)

admin.site.register(Etudiant, EtudiantAdmin)

"""
class ProfesseurInline(admin.StackedInline):
    model = Professeur
    can_delete = False
    verbose_name_plural = 'professeur'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfesseurInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

"""


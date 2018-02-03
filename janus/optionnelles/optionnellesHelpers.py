from django.contrib.auth.models import User

def getGroupTemplate(user):
    template = "" 
    if user.is_staff:
        if isInGroup("Professeur", user):
            template = "./optionnelles/menu_professeur_admin.html"
        else:
            template = "./optionnelles/menu_admin.html"
    else:
        if isInGroup("Professeur", user):
            template = "./optionnelles/menu_professeur.html"
        if isInGroup("Etudiant", user):
            template = "./optionnelles/menu_etudiant.html"
    return template

def isInGroup(groupe, user):
    res = User.objects.filter(pk=user.id, groups__name=groupe).exists()
    return res
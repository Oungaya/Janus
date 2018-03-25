
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Test

class Promotion(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Parcours(models.Model):
    nom = models.CharField(max_length=200)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class TypePole(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Pole(models.Model):
    nom = models.CharField(max_length=200)
    parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE)
    typePole = models.ForeignKey(TypePole, on_delete=models.CASCADE)
    nombre_options = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

class Semestre(models.Model):
    nom = models.CharField(max_length=200)
    diminutif = models.CharField(max_length=10)

    def __str__(self):
        return self.nom

class UE(models.Model):
    nom = models.CharField(max_length=200)
    num_UE = models.CharField(max_length=200)
    code_apoge = models.CharField(max_length=200)
    nombre_groupes = models.IntegerField(default=0)
    nombre_heures_TD = models.IntegerField(default=0)
    nombre_heures_CM = models.IntegerField(default=0)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    poles = models.ManyToManyField("Pole", through="UE_par_Pole")

    def __str__(self):
        return self.nom

class UE_par_Pole(models.Model):
    pole = models.ForeignKey(Pole, on_delete=models.CASCADE)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    option = models.BooleanField(default="False")

    def __str__(self):
        return self.ue.nom + " " + self.pole.nom

class Statut(models.Model):
    nom = models.CharField(max_length=200)
    nombre_heures = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

class Professeur(models.Model):
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE)
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    ues = models.ManyToManyField("UE", through="Professeur_par_UE")

    def __str__(self):
        return self.utilisateur.first_name + " " + self.utilisateur.last_name

class Professeur_par_UE(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    heuresCM = models.IntegerField(default=0)
    heuresTP = models.IntegerField(default=0)
    heuresTD = models.IntegerField(default=0)

    def __str__(self):
        return self.ue.nom + " " + self.professeur.nom + " " + self.professeur.prenom

class AnneeCourante(models.Model):
    parcours = models.ForeignKey(Parcours, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    dateDebutSemestre1 = models.DateTimeField('date début semestre 1')
    dateDebutSemestre2 = models.DateTimeField('date début semestre 2')
    dateFinSemestre1 = models.DateTimeField('date fin semestre 1')
    dateFinSemestre2 = models.DateTimeField('date fin semestre 2')
    dateDebutOptions1 = models.DateTimeField('date début options semestre 1')
    dateDebutOptions2 = models.DateTimeField('date début options semestre 2')
    dateFinOptions1 = models.DateTimeField('date fin options semestre 1')
    dateFinOptions2 = models.DateTimeField('date fin options semestre 2')
    dateDebutAnnee = models.DateTimeField('date début année')
    dateFinAnnee = models.DateTimeField('date fin année')

    def __str__(self):
        return self.nom



class Etudiant(models.Model):
    numero_etudiant = models.CharField(max_length=20)
    ajac = models.BooleanField(default="False")
    redoublant = models.BooleanField(default="False")
    #models.ForeignKey(Parcours, on_delete=models.CASCADE)
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    ues = models.ManyToManyField("UE", through="Etudiant_par_UE")
    parcours = models.ManyToManyField(Parcours)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.utilisateur.first_name + " " + self.utilisateur.last_name

class Etudiant_par_UE(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    optionnelle = models.BooleanField(default="False")
    groupe = models.IntegerField(default=0)
<<<<<<< HEAD
    order = models.IntegerField(default=0)
=======
    choisie = models.BooleanField(default="False")
>>>>>>> deploiement

    def __str__(self):
        return self.ue.nom + " " + self.etudiant.utilisateur.first_name + " " + self.etudiant.utilisateur.last_name

class Absence(models.Model):
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    date_heure = models.DateTimeField('date et heure')
    justifiee = models.BooleanField(default="False")

    def __str__(self):
        return self.prenom + " " + self.nom


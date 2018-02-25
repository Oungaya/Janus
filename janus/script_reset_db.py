#! /usr/bin/env python3
# coding: utf-8

import subprocess

def main():  
    subprocess.call('mysql -h 127.0.0.1 -P 8889 -u root -proot -e "DROP DATABASE janus; CREATE DATABASE janus;"', shell=True)
    subprocess.call('rm -r optionnelles/migrations/', shell=True)
    subprocess.call('python3 manage.py migrate', shell=True)
    subprocess.call('python3 manage.py makemigrations optionnelles', shell=True)
    subprocess.call('python3 manage.py migrate', shell=True)
    subprocess.call('mysql -h 127.0.0.1 -P 8889 -u root -proot -e "USE janus; INSERT INTO auth_group(name) VALUES (\'Etudiant\'); INSERT INTO auth_group(name) VALUES (\'Professeur\'); INSERT INTO optionnelles_statut(nom, nombre_heures) VALUES (\'Vacataire\', \'25\'); INSERT INTO optionnelles_promotion(nom) VALUES (\'M2\'); INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 SIS\', \'1\');"', shell=True)

if __name__ == "__main__":
   main()
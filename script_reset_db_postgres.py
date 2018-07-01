#! /usr/bin/env python3.7
# coding: utf-8

import subprocess

def main():  
    subprocess.call('psql -U postgres -h localhost -p 5432 -d janus -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE datname = \'janus\' AND pid <> pg_backend_pid();"', shell=True)
    #subprocess.call('sudo /etc/init.d/postgresql restart', shell=True)
    subprocess.call('dropdb -h localhost -p 5432 -U postgres janus', shell=True)
    subprocess.call('psql -U postgres -h localhost -p 5432 -c "CREATE DATABASE janus;"', shell=True)
    subprocess.call('rm -r optionnelles/migrations/', shell=True)
    subprocess.call('python manage.py migrate', shell=True)
    subprocess.call('python manage.py makemigrations optionnelles', shell=True)
    subprocess.call('python manage.py migrate', shell=True)
    subprocess.call('psql -U postgres -h localhost -p 5432 -d janus -c "\
    INSERT INTO auth_group(name) VALUES (\'Etudiant\');\
    INSERT INTO auth_group(name) VALUES (\'Professeur\');\
    INSERT INTO optionnelles_statut(nom, nombre_heures) VALUES (\'Vacataire\', \'25\');\
    INSERT INTO optionnelles_promotion(nom) VALUES (\'M1\');\
    INSERT INTO optionnelles_promotion(nom) VALUES (\'M2\');\
    INSERT INTO optionnelles_semestre(nom, diminutif) VALUES (\'Semestre 1\', \'S1\');\
    INSERT INTO optionnelles_semestre(nom, diminutif) VALUES (\'Semestre 2\', \'S2\');\
    INSERT INTO optionnelles_semestre(nom, diminutif) VALUES (\'Annuel\', \'AN\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M1 MIAGE Stage\', \'1\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M1 MIAGE Alternance\', \'1\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 OSIE\', \'2\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 SID\', \'2\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 SIO\', \'2\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 SIS\', \'2\');\
    INSERT INTO optionnelles_parcours(nom, promotion_id) VALUES (\'M2 INE\', \'2\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences en Ingénierie des SI\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences en Informatique\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences en Gestion\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Domaine d application\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences Transverses\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Professionnalisation\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'eSanté\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Ingénierie des SI\', \'1\', \'1\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Informatique\', \'1\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Domaine d''application\', \'1\', \'4\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences Transverses\', \'1\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Professionnalisation\', \'1\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Ingénierie des SI\', \'2\', \'1\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Informatique\', \'2\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Domaine d''application\', \'2\', \'4\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences Transverses\', \'2\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Professionnalisation\', \'2\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Ingénierie des SI\', \'3\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Informatique\', \'3\', \'2\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Gestion\', \'3\', \'3\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences Transverses\', \'3\', \'5\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Professionnalisation\', \'3\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Ingénierie des SI\', \'4\', \'1\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Informatique\', \'4\', \'2\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Gestion\', \'4\', \'3\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences Transverses\', \'4\', \'5\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SID Professionnalisation\', \'4\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Ingénierie des SI\', \'5\', \'1\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Informatique\', \'5\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Gestion\', \'5\', \'3\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences Transverses\', \'5\', \'5\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Professionnalisation\', \'5\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences en Ingénierie des SI\', \'6\', \'1\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences en Informatique\', \'6\', \'2\', \'1\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences Transverses\', \'6\', \'5\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIS eSanté\', \'6\', \'7\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Professionnalisation\', \'6\', \'6\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 INE Compétence en Ingénierie des SI\', \'7\', \'1\', \'0\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, type_pole_id, a_choisir_dans_pole) VALUES (\'M2 INE Professionnalisation\', \'7\', \'6\', \'3\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Conduite de projet\', \'ISI_02\', \'ISI_02\', \'0\', \'8\', \'40\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Ingénierie du logiciel\', \'ISI_05\', \'ISI_05\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Architecture client serveur\', \'ISI_01\', \'ISI_01\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Conduite du changement\', \'ISI_03\', \'ISI_03\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Contrôle qualité\', \'ISI_04\', \'ISI_04\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Analyse et décision en entreprise\', \'INFO_02\', \'INFO_02\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Architecture Web des SI\', \'INFO_03\', \'INFO_03\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Architecture des SI\', \'INFO_04\', \'INFO_04\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Administration des SE\', \'INFO_01\', \'INFO_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'ASI mobiles 1\', \'INFO_05\', \'INFO_05\', \'2\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'BD avancées\', \'INFO_06\', \'INFO_06\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Bio informatique 1\', \'INFO_07\', \'INFO_07\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Conception avancée des SI\', \'INFO_08\', \'INFO_08\', \'2\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'IHM\', \'INFO_09\', \'INFO_09\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Economie politique\', \'GEO_01\', \'GEO_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Marketing\', \'GEO_05\', \'GEO_05\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Analyse des systèmes physiques\', \'SANTE_01\', \'SANTE_01\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Notions de base en anatomie\', \'SANTE_04\', \'SANTE_04\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Gestion de production\', \'GEO_02\', \'GEO_02\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Marketing orienté Web\', \'GEO_06\', \'GEO_06\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Droit de la santé et bioéthique 1\', \'SANTE_02\', \'SANTE_02\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Anglais M1\', \'TRANS_01\', \'TRANS_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Découverte de la recherche\', \'TRANS_03\', \'TRANS_03\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Instrumentation biomédicale 1\', \'SANTE_03\', \'SANTE_03\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Communication\', \'TRANS_02\', \'TRANS_02\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Découverte des laboratoires\', \'TRANS_04\', \'TRANS_04\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Droit du travail\', \'TRANS_05\', \'TRANS_05\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Statistiques\', \'TRANS_06\', \'TRANS_06\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Projet Professionnel\', \'PRO_01\', \'PRO_01\', \'0\', \'8\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Audit des SI\', \'ISI_09\', \'ISI_09\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Progiciels de gestion intégrés\', \'ISI_11\', \'ISI_11\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Interopérabilité des SI (ETL)\', \'ISI_12\', \'ISI_12\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Conduite de projet agile\', \'ISI_14\', \'ISI_14\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Stratégie et management des SI\', \'ISI_15\', \'ISI_15\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Ingénierie des SI en santé\', \'ISI_16\', \'ISI_16\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Management de la sécurité des SI\', \'ISI_17\', \'ISI_17\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Workflows\', \'ISI_19\', \'ISI_19\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Architecture des SI 2\', \'INFO_18\', \'INFO_18\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'ASI Mobile 2\', \'INFO_19\', \'INFO_19\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Web Design\', \'INFO_31\', \'INFO_31\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Stratégie d entreprise\', \'GEO_08\', \'GEO_08\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Théories des organisations\', \'GEO_09\', \'GEO_09\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Anglais M2\', \'TRANS_08\', \'TRANS_08\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Environnement socio-économique\', \'TRANS_10\', \'TRANS_10\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Etude de cas thématique\', \'PRO_03\', \'PRO_03\', \'0\', \'0\', \'30\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Projet professionnel\', \'PRO_04\', \'PRO_04\', \'0\', \'0\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Outils pour la Business intelligence\', \'ISI_18\', \'ISI_18\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Outils pour les systèmes décisionnels en entreprise\', \'INFO_16\', \'INFO_16\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Aide à la décision avancée\', \'INFO_17\', \'INFO_17\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Modélis. des pb en management et mkg\', \'INFO_27\', \'INFO_27\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Recherche heuristique\', \'INFO_29\', \'INFO_29\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'IA\', \'INFO_23\', \'INFO_23\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Web x.0\', \'INFO_32\', \'INFO_32\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Data Science\', \'TRANS_09\', \'TRANS_09\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Big data\', \'INFO_20\', \'INFO_20\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Internet Of Things (IOT)\', \'INFO_26\', \'INFO_26\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Bio informatique 2\', \'INFO_21\', \'INFO_21\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Intelligence des systèmes biomédicaux\', \'INFO_25\', \'INFO_25\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Gestion de réseaux de capteurs biomédicaux\', \'INFO_22\', \'INFO_22\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Outils pour les données biomédicales\', \'INFO_28\', \'INFO_28\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Electrophysiologie\', \'SANTE_05\', \'SANTE_05\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Instrumentation biomédicale 2\', \'SANTE_06\', \'SANTE_06\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Télémédecine\', \'SANTE_07\', \'SANTE_07\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_ue, code_apoge, nombre_groupes, nombre_heures_cm, nombre_heures_td, semestre_id, capacite) VALUES (\'Etude de cas création d entreprise\', \'PRO_02\', \'PRO_02\', \'0\', \'0\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue_par_pole VALUES (1, \'f\',  1, 1);\
    INSERT INTO optionnelles_ue_par_pole VALUES (2, \'f\',  1, 2);\
    INSERT INTO optionnelles_ue_par_pole VALUES (3, \'t\',  1, 3);\
    INSERT INTO optionnelles_ue_par_pole VALUES (4, \'t\',  1, 4);\
    INSERT INTO optionnelles_ue_par_pole VALUES (5, \'t\',  1, 5);\
    INSERT INTO optionnelles_ue_par_pole VALUES (6, \'f\',  2, 6);\
    INSERT INTO optionnelles_ue_par_pole VALUES (7, \'f\',  2, 7);\
    INSERT INTO optionnelles_ue_par_pole VALUES (8, \'f\',  2, 8);\
    INSERT INTO optionnelles_ue_par_pole VALUES (9, \'t\',  2, 9);\
    INSERT INTO optionnelles_ue_par_pole VALUES (10, \'t\',  2, 10);\
    INSERT INTO optionnelles_ue_par_pole VALUES (11, \'t\',  2, 11);\
    INSERT INTO optionnelles_ue_par_pole VALUES (12, \'t\',  2, 12);\
    INSERT INTO optionnelles_ue_par_pole VALUES (13, \'t\',  2, 13);\
    INSERT INTO optionnelles_ue_par_pole VALUES (14, \'t\',  2, 14);\
    INSERT INTO optionnelles_ue_par_pole VALUES (15, \'f\',  3, 15);\
    INSERT INTO optionnelles_ue_par_pole VALUES (16, \'f\',  3, 16);\
    INSERT INTO optionnelles_ue_par_pole VALUES (17, \'f\',  3, 17);\
    INSERT INTO optionnelles_ue_par_pole VALUES (18, \'f\',  3, 18);\
    INSERT INTO optionnelles_ue_par_pole VALUES (19, \'t\',  3, 19);\
    INSERT INTO optionnelles_ue_par_pole VALUES (20, \'t\',  3, 20);\
    INSERT INTO optionnelles_ue_par_pole VALUES (21, \'t\',  3, 21);\
    INSERT INTO optionnelles_ue_par_pole VALUES (22, \'f\',  4, 22);\
    INSERT INTO optionnelles_ue_par_pole VALUES (23, \'f\',  4, 23);\
    INSERT INTO optionnelles_ue_par_pole VALUES (24, \'t\',  4, 24);\
    INSERT INTO optionnelles_ue_par_pole VALUES (25, \'t\',  4, 25);\
    INSERT INTO optionnelles_ue_par_pole VALUES (26, \'t\',  4, 26);\
    INSERT INTO optionnelles_ue_par_pole VALUES (27, \'t\',  4, 27);\
    INSERT INTO optionnelles_ue_par_pole VALUES (28, \'t\',  4, 28);\
    INSERT INTO optionnelles_ue_par_pole VALUES (29, \'f\',  5, 29);\
    INSERT INTO optionnelles_ue_par_pole VALUES (30, \'f\',  6, 1);\
    INSERT INTO optionnelles_ue_par_pole VALUES (31, \'f\',  6, 2);\
    INSERT INTO optionnelles_ue_par_pole VALUES (32, \'t\',  6, 3);\
    INSERT INTO optionnelles_ue_par_pole VALUES (34, \'t\',  6, 5);\
    INSERT INTO optionnelles_ue_par_pole VALUES (35, \'f\',  7, 6);\
    INSERT INTO optionnelles_ue_par_pole VALUES (36, \'f\',  7, 7);\
    INSERT INTO optionnelles_ue_par_pole VALUES (37, \'f\',  7, 8);\
    INSERT INTO optionnelles_ue_par_pole VALUES (38, \'t\',  7, 9);\
    INSERT INTO optionnelles_ue_par_pole VALUES (39, \'t\',  7, 10);\
    INSERT INTO optionnelles_ue_par_pole VALUES (40, \'t\',  7, 11);\
    INSERT INTO optionnelles_ue_par_pole VALUES (41, \'t\',  7, 12);\
    INSERT INTO optionnelles_ue_par_pole VALUES (42, \'t\',  7, 13);\
    INSERT INTO optionnelles_ue_par_pole VALUES (43, \'t\',  7, 14);\
    INSERT INTO optionnelles_ue_par_pole VALUES (44, \'f\',  8, 15);\
    INSERT INTO optionnelles_ue_par_pole VALUES (45, \'f\',  8, 16);\
    INSERT INTO optionnelles_ue_par_pole VALUES (46, \'f\',  8, 17);\
    INSERT INTO optionnelles_ue_par_pole VALUES (47, \'f\',  8, 18);\
    INSERT INTO optionnelles_ue_par_pole VALUES (48, \'t\',  8, 19);\
    INSERT INTO optionnelles_ue_par_pole VALUES (49, \'t\',  8, 20);\
    INSERT INTO optionnelles_ue_par_pole VALUES (50, \'t\',  8, 21);\
    INSERT INTO optionnelles_ue_par_pole VALUES (51, \'f\',  9, 22);\
    INSERT INTO optionnelles_ue_par_pole VALUES (52, \'f\',  9, 23);\
    INSERT INTO optionnelles_ue_par_pole VALUES (53, \'t\',  9, 24);\
    INSERT INTO optionnelles_ue_par_pole VALUES (54, \'t\',  9, 25);\
    INSERT INTO optionnelles_ue_par_pole VALUES (55, \'t\',  9, 26);\
    INSERT INTO optionnelles_ue_par_pole VALUES (56, \'t\',  9, 27);\
    INSERT INTO optionnelles_ue_par_pole VALUES (57, \'t\',  9, 28);\
    INSERT INTO optionnelles_ue_par_pole VALUES (58, \'f\',  10, 29);\
    INSERT INTO optionnelles_ue_par_pole VALUES (59, \'f\',  11, 30);\
    INSERT INTO optionnelles_ue_par_pole VALUES (60, \'f\',  11, 31);\
    INSERT INTO optionnelles_ue_par_pole VALUES (61, \'f\',  11, 32);\
    INSERT INTO optionnelles_ue_par_pole VALUES (62, \'f\',  11, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (63, \'f\',  11, 34);\
    INSERT INTO optionnelles_ue_par_pole VALUES (64, \'t\',  11, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (65, \'t\',  11, 36);\
    INSERT INTO optionnelles_ue_par_pole VALUES (66, \'t\',  11, 37);\
    INSERT INTO optionnelles_ue_par_pole VALUES (67, \'f\',  12, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (68, \'t\',  12, 39);\
    INSERT INTO optionnelles_ue_par_pole VALUES (69, \'t\',  12, 40);\
    INSERT INTO optionnelles_ue_par_pole VALUES (70, \'f\',  13, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (71, \'f\',  13, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (72, \'f\',  14, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (73, \'f\',  14, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (74, \'f\',  15, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (75, \'f\',  15, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (76, \'f\',  16, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (77, \'f\',  16, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (78, \'f\',  17, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (79, \'f\',  17, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (80, \'f\',  17, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (81, \'f\',  17, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (82, \'f\',  17, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (83, \'t\',  17, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (84, \'t\',  17, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (85, \'f\',  18, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (86, \'f\',  18, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (87, \'f\',  19, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (88, \'f\',  19, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (89, \'f\',  19, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (90, \'f\',  20, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (91, \'f\',  20, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (92, \'f\',  21, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (93, \'f\',  21, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (94, \'f\',  22, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (95, \'f\',  22, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (96, \'f\',  22, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (97, \'f\',  22, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (98, \'f\',  22, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (99, \'t\',  22, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (100, \'t\',  22, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (101, \'f\',  23, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (102, \'f\',  23, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (103, \'f\',  24, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (104, \'f\',  24, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (105, \'f\',  24, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (106, \'f\',  25, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (107, \'f\',  25, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (108, \'f\',  26, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (109, \'f\',  26, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (110, \'f\',  27, 57);\
    INSERT INTO optionnelles_ue_par_pole VALUES (111, \'f\',  27, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (112, \'f\',  27, 58);\
    INSERT INTO optionnelles_ue_par_pole VALUES (113, \'f\',  27, 56);\
    INSERT INTO optionnelles_ue_par_pole VALUES (114, \'t\',  27, 59);\
    INSERT INTO optionnelles_ue_par_pole VALUES (115, \'t\',  27, 60);\
    INSERT INTO optionnelles_ue_par_pole VALUES (116, \'f\',  28, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (117, \'f\',  28, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (118, \'f\',  28, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (119, \'f\',  29, 61);\
    INSERT INTO optionnelles_ue_par_pole VALUES (120, \'f\',  29, 62);\
    INSERT INTO optionnelles_ue_par_pole VALUES (121, \'f\',  29, 63);\
    INSERT INTO optionnelles_ue_par_pole VALUES (122, \'f\',  30, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (123, \'f\',  30, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (124, \'f\',  31, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (125, \'f\',  31, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (126, \'f\',  32, 64);\
    INSERT INTO optionnelles_ue_par_pole VALUES (127, \'f\',  32, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (128, \'t\',  32, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (129, \'t\',  32, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (130, \'t\',  32, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (131, \'t\',  32, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (132, \'t\',  32, 39);\
    INSERT INTO optionnelles_ue_par_pole VALUES (133, \'t\',  32, 55);\
    INSERT INTO optionnelles_ue_par_pole VALUES (134, \'t\',  32, 57);\
    INSERT INTO optionnelles_ue_par_pole VALUES (135, \'t\',  32, 59);\
    INSERT INTO optionnelles_ue_par_pole VALUES (136, \'t\',  32, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (137, \'t\',  32, 58);\
    INSERT INTO optionnelles_ue_par_pole VALUES (138, \'t\',  32, 56);\
    INSERT INTO optionnelles_ue_par_pole VALUES (139, \'t\',  32, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (140, \'t\',  32, 60);\
    INSERT INTO optionnelles_ue_par_pole VALUES (141, \'t\',  32, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (142, \'t\',  32, 40);\
    INSERT INTO optionnelles_ue_par_pole VALUES (143, \'t\',  32, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (144, \'t\',  32, 31);\
    INSERT INTO optionnelles_ue_par_pole VALUES (145, \'t\',  32, 32);\
    INSERT INTO optionnelles_ue_par_pole VALUES (146, \'t\',  32, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (147, \'t\',  32, 36);\
    INSERT INTO optionnelles_ue_par_pole VALUES (148, \'t\',  32, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (149, \'t\',  32, 61);\
    INSERT INTO optionnelles_ue_par_pole VALUES (150, \'t\',  32, 62);\
    INSERT INTO optionnelles_ue_par_pole VALUES (151, \'t\',  32, 63);\
    INSERT INTO optionnelles_ue_par_pole VALUES (152, \'t\',  32, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (153, \'t\',  32, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (154, \'t\',  32, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (155, \'t\',  21, 36);\
    INSERT INTO optionnelles_ue_par_pole VALUES (156, \'t\',  21, 37);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 1, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 1, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 2, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (4, 2, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 3, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 3, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 4, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 4, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 5, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 6, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 6, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 7, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (4, 7, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 8, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 8, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 9, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 9, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 10, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 11, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 11, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 12, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 12, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 13, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 13, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 14, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 14, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 15, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 16, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 16, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 17, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 17, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 18, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 18, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 19, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 19, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 20, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 21, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 21, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 22, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 22, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 23, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 23, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 24, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 24, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 25, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 26, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 26, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 27, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 27, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 28, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 28, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 29, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 29, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 30, 3);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 31, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 31, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (14, 32, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (13, 32, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (0, 32, 3);\
    "', shell=True)
    subprocess.call('python manage.py createsuperuser', shell=True)

if __name__ == "__main__":
   main()
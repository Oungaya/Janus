#! /usr/bin/env python3
# coding: utf-8

import subprocess

def main():  
    subprocess.call('mysql -h 127.0.0.1 -P 8889 -u root -proot -e "DROP DATABASE janus; CREATE DATABASE janus;"', shell=True)
    subprocess.call('rm -r optionnelles/migrations/', shell=True)
    subprocess.call('python3 manage.py migrate', shell=True)
    subprocess.call('python3 manage.py makemigrations optionnelles', shell=True)
    subprocess.call('python3 manage.py migrate', shell=True)
    subprocess.call('mysql -h 127.0.0.1 -P 8889 -u root -proot -e "\
    USE janus;\
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
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Domaine d''application\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences Transverses\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Professionnalisation\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'eSanté\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M1 MIAGE Compétences en Ingénierie des SI\', \'3\', \'1\', \'1\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M1 MIAGE Compétences en Informatique\', \'6\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M1 MIAGE Domaine d''application\', \'3\', \'1\', \'4\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M1 MIAGE Compétences Transverses\', \'5\', \'1\', \'5\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M1 MIAGE Professionnalisation\', \'0\', \'1\', \'6\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 OSIE Compétences en Ingénierie des SI\', \'3\', \'2\', \'1\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 OSIE Compétences en Informatique\', \'2\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 OSIE Compétences en Gestion\', \'0\', \'2\', \'3\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 OSIE Compétences Transverses\', \'0\', \'2\', \'5\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 OSIE Professionnalisation\', \'0\', \'2\', \'6\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SID Compétences en Ingénierie des SI\', \'0\', \'3\', \'1\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SID Compétences en Informatique\', \'2\', \'3\', \'2\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SID Compétences en Gestion\', \'0\', \'3\', \'3\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SID Compétences Transverses\', \'0\', \'3\', \'5\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SID Professionnalisation\', \'0\', \'3\', \'6\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIO Compétences en Ingénierie des SI\', \'2\', \'4\', \'1\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIO Compétences en Informatique\', \'3\', \'4\', \'2\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIO Compétences en Gestion\', \'0\', \'4\', \'3\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIO Compétences Transverses\', \'0\', \'4\', \'5\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIO Professionnalisation\', \'0\', \'4\', \'6\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIS Compétences en Ingénierie des SI\', \'0\', \'5\', \'1\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIS Compétences en Informatique\', \'2\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIS Compétences Transverses\', \'0\', \'5\', \'5\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIS eSanté\', \'0\', \'5\', \'7\');\
    INSERT INTO optionnelles_pole(nom, nombre_options, parcours_id, typePole_id) VALUES (\'M2 SIS Professionnalisation\', \'0\', \'5\', \'6\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Conduite de projet\', \'ISI_02\', \'0\', \'0\', \'8\', \'40\', \'3\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Ingénierie du logiciel\', \'ISI_05\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Architecture client serveur\', \'ISI_01\', \'0\', \'2\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Conduite du changement\', \'ISI_03\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Contrôle qualité\', \'ISI_04\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Analyse et décision en entreprise\', \'INFO_02\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Architecture Web des SI\', \'INFO_03\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Architecture des SI\', \'INFO_04\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Administration des SE\', \'INFO_01\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'ASI mobiles 1\', \'INFO_05\', \'0\', \'2\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'BD avancées\', \'INFO_06\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Bio informatique 1\', \'INFO_07\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Conception avancée des SI\', \'INFO_08\', \'0\', \'2\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'IHM\', \'INFO_09\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Economie politique\', \'GEO_01\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Marketing\', \'GEO_05\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Analyse des systèmes physiques\', \'SANTE_01\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Notions de base en anatomie\', \'SANTE_04\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Gestion de production\', \'GEO_02\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Marketing orienté Web\', \'GEO_06\', \'0\', \'2\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Droit de la santé et bioéthique 1\', \'SANTE_02\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Anglais\', \'TRANS_01\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Découverte de la recherche\', \'TRANS_03\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Instrumentation biomédicale 1\', \'SANTE_03\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Communication\', \'TRANS_02\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Découverte des laboratoires\', \'TRANS_04\', \'0\', \'2\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Droit du travail\', \'TRANS_05\', \'0\', \'2\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Statistiques\', \'TRANS_06\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Projet Professionnel\', \'PRO_01\', \'0\', \'0\', \'8\', \'0\', \'3\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Audit des SI\', \'ISI_09\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Progiciels de gestion intégrés\', \'ISI_11\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Interopérabilité des SI (ETL)\', \'ISI_12\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Conduite de projet agile\', \'ISI_14\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Stratégie et management des SI\', \'ISI_15\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Ingénierie des SI en santé\', \'ISI_16\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Management de la sécurité des SI\', \'ISI_17\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Workflows\', \'ISI_19\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Architecture des SI 2\', \'INFO_18\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'ASI Mobile 2\', \'INFO_19\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Web Design\', \'INFO_31\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Stratégie d''entreprise\', \'GEO_08\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Théories des organisations\', \'GEO_09\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Anglais\', \'TRANS_08\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Environnement socio-économique\', \'TRANS_10\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Etude de cas thématique\', \'PRO_03\', \'0\', \'0\', \'0\', \'30\', \'3\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Projet professionnel\', \'PRO_04\', \'0\', \'0\', \'0\', \'0\', \'3\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Outils pour la Business intelligence\', \'ISI_18\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Outils pour les systèmes décisionnels en entreprise\', \'INFO_16\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Aide à la décision avancée\', \'INFO_17\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Architecture des SI 2\', \'INFO_18\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Modélis. des pb en management et mkg\', \'INFO_27\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Recherche heuristique\', \'INFO_29\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'IA\', \'INFO_23\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Web x.0\', \'INFO_32\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Data Science\', \'TRANS_09\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Big data\', \'INFO_20\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Internet Of Things (IOT)\', \'INFO_26\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Bio informatique 2\', \'INFO_21\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Intelligence des systèmes biomédicaux\', \'INFO_25\', \'0\', \'0\', \'8\', \'22\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Gestion de réseaux de capteurs biomédicaux\', \'INFO_22\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Outils pour les données biomédicales\', \'INFO_28\', \'0\', \'0\', \'8\', \'22\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Electrophysiologie\', \'SANTE_05\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Instrumentation biomédicale 2\', \'SANTE_06\', \'0\', \'0\', \'0\', \'30\', \'1\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id) VALUES (\'Télémédecine\', \'SANTE_07\', \'0\', \'0\', \'0\', \'30\', \'2\');\
    "', shell=True)
    subprocess.call('python3 manage.py createsuperuser', shell=True)

if __name__ == "__main__":
   main()
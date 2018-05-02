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
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Domaine d application\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Compétences Transverses\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'Professionnalisation\');\
    INSERT INTO optionnelles_typepole(nom) VALUES (\'eSanté\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Ingénierie des SI\', \'1\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Informatique\', \'1\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Domaine d''application\', \'1\', \'4\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences Transverses\', \'1\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Professionnalisation\', \'1\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Ingénierie des SI\', \'2\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences en Informatique\', \'2\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Domaine d''application\', \'2\', \'4\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Compétences Transverses\', \'2\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M1 MIAGE Professionnalisation\', \'2\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Ingénierie des SI\', \'3\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Informatique\', \'3\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences en Gestion\', \'3\', \'3\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Compétences Transverses\', \'3\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 OSIE Professionnalisation\', \'3\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Ingénierie des SI\', \'4\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Informatique\', \'4\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences en Gestion\', \'4\', \'3\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SID Compétences Transverses\', \'4\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SID Professionnalisation\', \'4\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Ingénierie des SI\', \'5\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Informatique\', \'5\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences en Gestion\', \'5\', \'3\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Compétences Transverses\', \'5\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIO Professionnalisation\', \'5\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences en Ingénierie des SI\', \'6\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences en Informatique\', \'6\', \'2\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Compétences Transverses\', \'6\', \'5\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIS eSanté\', \'6\', \'7\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 SIS Professionnalisation\', \'6\', \'6\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 INE Compétence en Ingénierie des SI\', \'7\', \'1\', \'2\');\
    INSERT INTO optionnelles_pole(nom, parcours_id, typePole_id, a_choisir_dans_pole) VALUES (\'M2 INE Professionnalisation\', \'7\', \'6\', \'2\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Conduite de projet\', \'ISI_02\', \'ISI_02\', \'0\', \'8\', \'40\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Ingénierie du logiciel\', \'ISI_05\', \'ISI_05\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Architecture client serveur\', \'ISI_01\', \'ISI_01\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Conduite du changement\', \'ISI_03\', \'ISI_03\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Contrôle qualité\', \'ISI_04\', \'ISI_04\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Analyse et décision en entreprise\', \'INFO_02\', \'INFO_02\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Architecture Web des SI\', \'INFO_03\', \'INFO_03\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Architecture des SI\', \'INFO_04\', \'INFO_04\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Administration des SE\', \'INFO_01\', \'INFO_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'ASI mobiles 1\', \'INFO_05\', \'INFO_05\', \'2\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'BD avancées\', \'INFO_06\', \'INFO_06\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Bio informatique 1\', \'INFO_07\', \'INFO_07\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Conception avancée des SI\', \'INFO_08\', \'INFO_08\', \'2\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'IHM\', \'INFO_09\', \'INFO_09\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Economie politique\', \'GEO_01\', \'GEO_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Marketing\', \'GEO_05\', \'GEO_05\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Analyse des systèmes physiques\', \'SANTE_01\', \'SANTE_01\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Notions de base en anatomie\', \'SANTE_04\', \'SANTE_04\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Gestion de production\', \'GEO_02\', \'GEO_02\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Marketing orienté Web\', \'GEO_06\', \'GEO_06\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Droit de la santé et bioéthique 1\', \'SANTE_02\', \'SANTE_02\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Anglais M1\', \'TRANS_01\', \'TRANS_01\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Découverte de la recherche\', \'TRANS_03\', \'TRANS_03\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Instrumentation biomédicale 1\', \'SANTE_03\', \'SANTE_03\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Communication\', \'TRANS_02\', \'TRANS_02\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Découverte des laboratoires\', \'TRANS_04\', \'TRANS_04\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Droit du travail\', \'TRANS_05\', \'TRANS_05\', \'2\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Statistiques\', \'TRANS_06\', \'TRANS_06\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Projet Professionnel\', \'PRO_01\', \'PRO_01\', \'0\', \'8\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Audit des SI\', \'ISI_09\', \'ISI_09\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Progiciels de gestion intégrés\', \'ISI_11\', \'ISI_11\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Interopérabilité des SI (ETL)\', \'ISI_12\', \'ISI_12\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Conduite de projet agile\', \'ISI_14\', \'ISI_14\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Stratégie et management des SI\', \'ISI_15\', \'ISI_15\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Ingénierie des SI en santé\', \'ISI_16\', \'ISI_16\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Management de la sécurité des SI\', \'ISI_17\', \'ISI_17\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Workflows\', \'ISI_19\', \'ISI_19\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Architecture des SI 2\', \'INFO_18\', \'INFO_18\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'ASI Mobile 2\', \'INFO_19\', \'INFO_19\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Web Design\', \'INFO_31\', \'INFO_31\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Stratégie d entreprise\', \'GEO_08\', \'GEO_08\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Théories des organisations\', \'GEO_09\', \'GEO_09\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Anglais M2\', \'TRANS_08\', \'TRANS_08\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Environnement socio-économique\', \'TRANS_10\', \'TRANS_10\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Etude de cas thématique\', \'PRO_03\', \'PRO_03\', \'0\', \'0\', \'30\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Projet professionnel\', \'PRO_04\', \'PRO_04\', \'0\', \'0\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Outils pour la Business intelligence\', \'ISI_18\', \'ISI_18\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Outils pour les systèmes décisionnels en entreprise\', \'INFO_16\', \'INFO_16\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Aide à la décision avancée\', \'INFO_17\', \'INFO_17\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Modélis. des pb en management et mkg\', \'INFO_27\', \'INFO_27\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Recherche heuristique\', \'INFO_29\', \'INFO_29\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'IA\', \'INFO_23\', \'INFO_23\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Web x.0\', \'INFO_32\', \'INFO_32\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Data Science\', \'TRANS_09\', \'TRANS_09\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Big data\', \'INFO_20\', \'INFO_20\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Internet Of Things (IOT)\', \'INFO_26\', \'INFO_26\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Bio informatique 2\', \'INFO_21\', \'INFO_21\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Intelligence des systèmes biomédicaux\', \'INFO_25\', \'INFO_25\', \'0\', \'8\', \'22\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Gestion de réseaux de capteurs biomédicaux\', \'INFO_22\', \'INFO_22\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Outils pour les données biomédicales\', \'INFO_28\', \'INFO_28\', \'0\', \'8\', \'22\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Electrophysiologie\', \'SANTE_05\', \'SANTE_05\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Instrumentation biomédicale 2\', \'SANTE_06\', \'SANTE_06\', \'0\', \'0\', \'30\', \'1\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Télémédecine\', \'SANTE_07\', \'SANTE_07\', \'0\', \'0\', \'30\', \'2\', \'20\');\
    INSERT INTO optionnelles_ue(nom, num_UE, code_apoge, nombre_groupes, nombre_heures_CM, nombre_heures_TD, semestre_id, capacite) VALUES (\'Etude de cas création d entreprise\', \'PRO_02\', \'PRO_02\', \'0\', \'0\', \'0\', \'3\', \'20\');\
    INSERT INTO optionnelles_ue_par_pole VALUES (1, 0, 1, 1);\
    INSERT INTO optionnelles_ue_par_pole VALUES (2, 0, 1, 2);\
    INSERT INTO optionnelles_ue_par_pole VALUES (3, 1, 1, 3);\
    INSERT INTO optionnelles_ue_par_pole VALUES (4, 1, 1, 4);\
    INSERT INTO optionnelles_ue_par_pole VALUES (5, 1, 1, 5);\
    INSERT INTO optionnelles_ue_par_pole VALUES (6, 0, 2, 6);\
    INSERT INTO optionnelles_ue_par_pole VALUES (7, 0, 2, 7);\
    INSERT INTO optionnelles_ue_par_pole VALUES (8, 0, 2, 8);\
    INSERT INTO optionnelles_ue_par_pole VALUES (9, 1, 2, 9);\
    INSERT INTO optionnelles_ue_par_pole VALUES (10, 1, 2, 10);\
    INSERT INTO optionnelles_ue_par_pole VALUES (11, 1, 2, 11);\
    INSERT INTO optionnelles_ue_par_pole VALUES (12, 1, 2, 12);\
    INSERT INTO optionnelles_ue_par_pole VALUES (13, 1, 2, 13);\
    INSERT INTO optionnelles_ue_par_pole VALUES (14, 1, 2, 14);\
    INSERT INTO optionnelles_ue_par_pole VALUES (15, 0, 3, 15);\
    INSERT INTO optionnelles_ue_par_pole VALUES (16, 0, 3, 16);\
    INSERT INTO optionnelles_ue_par_pole VALUES (17, 0, 3, 17);\
    INSERT INTO optionnelles_ue_par_pole VALUES (18, 0, 3, 18);\
    INSERT INTO optionnelles_ue_par_pole VALUES (19, 1, 3, 19);\
    INSERT INTO optionnelles_ue_par_pole VALUES (20, 1, 3, 20);\
    INSERT INTO optionnelles_ue_par_pole VALUES (21, 1, 3, 21);\
    INSERT INTO optionnelles_ue_par_pole VALUES (22, 0, 4, 22);\
    INSERT INTO optionnelles_ue_par_pole VALUES (23, 0, 4, 23);\
    INSERT INTO optionnelles_ue_par_pole VALUES (24, 1, 4, 24);\
    INSERT INTO optionnelles_ue_par_pole VALUES (25, 1, 4, 25);\
    INSERT INTO optionnelles_ue_par_pole VALUES (26, 1, 4, 26);\
    INSERT INTO optionnelles_ue_par_pole VALUES (27, 1, 4, 27);\
    INSERT INTO optionnelles_ue_par_pole VALUES (28, 1, 4, 28);\
    INSERT INTO optionnelles_ue_par_pole VALUES (29, 0, 5, 29);\
    INSERT INTO optionnelles_ue_par_pole VALUES (30, 0, 6, 30);\
    INSERT INTO optionnelles_ue_par_pole VALUES (31, 0, 6, 31);\
    INSERT INTO optionnelles_ue_par_pole VALUES (32, 0, 6, 32);\
    INSERT INTO optionnelles_ue_par_pole VALUES (33, 0, 6, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (34, 0, 6, 34);\
    INSERT INTO optionnelles_ue_par_pole VALUES (35, 1, 6, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (36, 1, 6, 36);\
    INSERT INTO optionnelles_ue_par_pole VALUES (37, 1, 6, 37);\
    INSERT INTO optionnelles_ue_par_pole VALUES (38, 0, 7, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (39, 1, 7, 39);\
    INSERT INTO optionnelles_ue_par_pole VALUES (40, 1, 7, 40);\
    INSERT INTO optionnelles_ue_par_pole VALUES (41, 0, 8, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (42, 0, 8, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (43, 0, 9, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (44, 0, 9, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (45, 0, 10, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (46, 0, 10, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (47, 0, 11, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (49, 0, 11, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (50, 0, 12, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (51, 0, 12, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (52, 0, 12, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (53, 0, 12, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (54, 0, 12, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (55, 1, 12, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (56, 1, 12, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (57, 0, 13, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (58, 0, 13, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (59, 0, 14, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (60, 0, 14, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (61, 0, 14, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (62, 0, 15, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (63, 0, 15, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (64, 0, 16, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (65, 0, 16, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (66, 0, 17, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (67, 0, 17, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (68, 0, 17, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (69, 0, 17, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (70, 0, 17, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (71, 1, 17, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (72, 1, 17, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (73, 0, 18, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (74, 0, 18, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (75, 0, 19, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (76, 0, 19, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (77, 0, 19, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (78, 0, 20, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (79, 0, 20, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (80, 0, 21, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (81, 0, 21, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (82, 0, 22, 57);\
    INSERT INTO optionnelles_ue_par_pole VALUES (83, 0, 22, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (84, 0, 22, 58);\
    INSERT INTO optionnelles_ue_par_pole VALUES (85, 0, 22, 56);\
    INSERT INTO optionnelles_ue_par_pole VALUES (86, 1, 22, 59);\
    INSERT INTO optionnelles_ue_par_pole VALUES (87, 1, 22, 60);\
    INSERT INTO optionnelles_ue_par_pole VALUES (88, 0, 23, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (89, 0, 23, 44);\
    INSERT INTO optionnelles_ue_par_pole VALUES (90, 0, 23, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (91, 0, 24, 61);\
    INSERT INTO optionnelles_ue_par_pole VALUES (92, 0, 24, 62);\
    INSERT INTO optionnelles_ue_par_pole VALUES (93, 0, 24, 63);\
    INSERT INTO optionnelles_ue_par_pole VALUES (94, 0, 25, 45);\
    INSERT INTO optionnelles_ue_par_pole VALUES (95, 0, 25, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (96, 0, 26, 33);\
    INSERT INTO optionnelles_ue_par_pole VALUES (97, 0, 26, 41);\
    INSERT INTO optionnelles_ue_par_pole VALUES (98, 0, 27, 64);\
    INSERT INTO optionnelles_ue_par_pole VALUES (99, 0, 27, 46);\
    INSERT INTO optionnelles_ue_par_pole VALUES (100, 1, 27, 42);\
    INSERT INTO optionnelles_ue_par_pole VALUES (101, 1, 27, 48);\
    INSERT INTO optionnelles_ue_par_pole VALUES (102, 1, 27, 49);\
    INSERT INTO optionnelles_ue_par_pole VALUES (103, 1, 27, 38);\
    INSERT INTO optionnelles_ue_par_pole VALUES (104, 1, 27, 39);\
    INSERT INTO optionnelles_ue_par_pole VALUES (105, 1, 27, 55);\
    INSERT INTO optionnelles_ue_par_pole VALUES (106, 1, 27, 57);\
    INSERT INTO optionnelles_ue_par_pole VALUES (107, 1, 27, 59);\
    INSERT INTO optionnelles_ue_par_pole VALUES (108, 1, 27, 52);\
    INSERT INTO optionnelles_ue_par_pole VALUES (109, 1, 27, 58);\
    INSERT INTO optionnelles_ue_par_pole VALUES (110, 1, 27, 56);\
    INSERT INTO optionnelles_ue_par_pole VALUES (111, 1, 27, 50);\
    INSERT INTO optionnelles_ue_par_pole VALUES (112, 1, 27, 60);\
    INSERT INTO optionnelles_ue_par_pole VALUES (113, 1, 27, 51);\
    INSERT INTO optionnelles_ue_par_pole VALUES (114, 1, 27, 40);\
    INSERT INTO optionnelles_ue_par_pole VALUES (115, 1, 27, 53);\
    INSERT INTO optionnelles_ue_par_pole VALUES (116, 1, 27, 31);\
    INSERT INTO optionnelles_ue_par_pole VALUES (117, 1, 27, 32);\
    INSERT INTO optionnelles_ue_par_pole VALUES (118, 1, 27, 35);\
    INSERT INTO optionnelles_ue_par_pole VALUES (119, 1, 27, 36);\
    INSERT INTO optionnelles_ue_par_pole VALUES (120, 1, 27, 47);\
    INSERT INTO optionnelles_ue_par_pole VALUES (121, 1, 27, 61);\
    INSERT INTO optionnelles_ue_par_pole VALUES (122, 1, 27, 62);\
    INSERT INTO optionnelles_ue_par_pole VALUES (123, 1, 27, 63);\
    INSERT INTO optionnelles_ue_par_pole VALUES (124, 1, 27, 43);\
    INSERT INTO optionnelles_ue_par_pole VALUES (125, 1, 27, 54);\
    INSERT INTO optionnelles_ue_par_pole VALUES (126, 1, 27, 44);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 1, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 2, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (4, 2, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 3, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 4, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 4, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 6, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 7, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (4, 7, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 8, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 9, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 9, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 11, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 12, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 17, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 21, 2);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (3, 22, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (2, 27, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (14, 32, 1);\
    INSERT INTO optionnelles_pole_par_semestre(nombre_options, pole_id, semestre_id) VALUES (13, 32, 2);\
    "', shell=True)
    subprocess.call('python3 manage.py createsuperuser', shell=True)

if __name__ == "__main__":
   main()
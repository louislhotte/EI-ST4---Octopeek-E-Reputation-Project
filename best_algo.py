import csv
import numpy as np
import pandas as pd
from math import sqrt


Path = []  # Liste des paths
Unknown = []
Positive = []
Negative = []
Neutral = []


def create_dic(Path):
    """
    :param dataset:     CSV avec pseudos, scores et abonnements (Normalement, 2 CSV différent?)
    :return:            dic_score : {Pseudo : "Score"}
                        dic = {Abonnement : "Pseudo"}
    """
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            Unknown.append(row)

    Pseudos = []
    # On va créer une liste de liste Pseudos, avec en Pseudo[i][0] = Pseudo et Pseudo[i][1] = 0, -1, 1
    # en fonction de sa positivité
    # Et Pseudo[i][2] va correspondre à la liste de ses abonnements

    # [A insérer, remplissage de Pseudos]

    dic_score = {}
    dic = {}
    n = len(Pseudos)
    for i in range(n):
        dic_score[Pseudos[i][0]] = Pseudos[i][1]
        for x in Pseudos[i][2]:
            if x not in dic:
                dic[x] = [Pseudos[i][0]]
            else:
                dic[x].append(Pseudos[i][0])


def loop(follow, Unkwown, Label):
    """
    :Input: Matrice utilisateurs/abonnements remplie actuellement appelée "follow", Liste Unknown, Matrice Label des pseudos labellisés "pour",
    "contre", ou "neutre" à propos d'Elon.
    :return: Matrice follow agrandie (avec les fortements positif, fortements neutre,
    fortement négatif rentrant dans la matrice), liste Unknown modifiée avec les pseudos qui sont
    entrés dans la matrice follow : ils sont supprimés de Unknown
    """

    return


def main(Unknown, dataset):
    """
    :param: dataset (Dataset avec les pseudos des individus labellisés "Pro-ElonMusk" et "Anti-ElonMusk")
    Unknown (la liste des pseudos non 'classés')
    :return: Dictionnaire ou matrice qui à chaque pseudo associe son statut 'Positif', 'Neutre' ou 'Négatif'
    """
    Compteur = 0

    while len(Unknown) > 0:
        follow = loop(Unknown)
        Compteur += 1

        # Si l'ordi n'arrive
        if Compteur > 100:
            break

    # Puis une fois qu'on a la matrice follow finale, il faut créer la matrice de similarité

    return


def calcul_sim(dic, user_1, user_2):
    user_1_number = 0
    user_2_number = 0

    sim = 0

    for items in dic.items():
        is_in_1 = user_1 in items[1]
        is_in_2 = user_2 in items[1]
        if is_in_1:
            user_1_number += 1
        if is_in_2:
            user_2_number += 1

        if is_in_1 and is_in_2:
            sim += 1

    return sim/(sqrt(user_1_number)*sqrt(user_2_number))


def vect_sim(dic_score, dic, user):
    pass
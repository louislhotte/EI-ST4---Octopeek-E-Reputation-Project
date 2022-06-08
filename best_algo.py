import csv
import numpy as np
import pandas as pd
from math import sqrt


Path = 'datapart14.csv'
Unknown = []
Positive = []
Negative = []
Neutral = []


def create_dic(Path):
    """
    :param dataset:     CSV
    :return:            dic_score : {Pseudo : "Score"}
                        dic = {Abonnement : "Pseudo"}
    """
    Pseudos = []
    with open(Path, newline='') as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            if row != []:
                pseudo = row[0]
                list = row[1][1:].split(', ')
                n = len(list)
                for i in range(len(list) - 1):
                    list[i] = int(list[i])
                last_follower = int(list[n - 1].split(']')[0])
                score = list[0]
                followers = list[1:n - 2]
                followers.append(last_follower)
                Pseudos.append([pseudo, score, followers])

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


def calcul_sim(dic, new_user, new_user_following, user):
     new_user_number = 0
     user_number = 0

     sim = 0

     for following in new_user_following:
          new_user_number += 1
          if user in dic[following]:
               sim += 1

     
     for items in dic.items():
          if user in items[1]:
               user_number += 1

     return sim/(sqrt(new_user_number)*sqrt(user_number))


def vect_sim(dic_score, dic, new_user):
     user_sim_dic = dict()
     for user in dic_score:
          user_sim_dic[user] = calcul_sim(dic, new_user, user)
     return user_sim_dic

def score_prediction(dic_score, new_user, new_sim_dic):
     score = 0;
     denominateur = 0
     
     for user in dic_score:
          score += dic_score[user]*new_sim_dic[user]
          denominateur += abs(new_sim_dic[user])
     
     return score/denominateur



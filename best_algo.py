import csv
import numpy as np
import pandas as pd
from math import sqrt


Path = 'datapart14.csv'


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
    return dic_score, dic


def convert_CSV_into_unknown(CSV_path):
     """
     :param CSV_path:
     :return: dic {Pseudo : "Abonnements"}
     """
     dict = {}
     with open(CSV_path, newline='') as csvfile:
          read = csv.reader(csvfile)
          for row in read:
               if row != []:
                    pseudo = int(row[0])
                    list = row[1][1:].split(', ')
                    n = len(list)
                    for i in range(len(list) - 1):
                         list[i] = int(list[i])

                    last_follower = int(list[n - 1].split(']')[0])
                    followers = list[1:n - 2]
                    followers.append(last_follower)
                    print(followers)

                    dict[pseudo] = followers

     return dict


def convert_dic_into_CSV(dic, name):
     with open(name+'.csv', 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=[key for key in dic])
          writer.writeheader()
          writer.writerows([dic])


def main(dic, dic_score, unknown):
     """
     :param dic: {Abonnement : "Pseudo"}
     :param dic_score: {Pseudo : "Score"}
     :param unknown: Dictionnaire {Pseudo : "Abonnements"}
     :return: ø
     """
     Compteur = 0
     while len(unknown) > 0:

         for user in unknown:
              user_vect_sim = vect_sim(dic_score, dic, user)
              score = score_prediction(dic_score, user, user_vect_sim)
              if test_score_user(score) != None:
                   dic_score[user] = score
                   dic[user] = unknown[user]
                   unknown.pop(user)
         Compteur += 1

         if Compteur == 20:
              break

     with open('dic_score.csv', 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=[key for key in dic_score])
          writer.writeheader()
          writer.writerows([dic_score])
     
     convert_dic_into_CSV(dic_score, 'dic_score')
     convert_dic_into_CSV(dic, 'dic')
     convert_dic_into_CSV(unknown, 'unknown')

     with open('unknown.csv', 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=[key for key in unknown])
          writer.writeheader()
          writer.writerows([unknown])

def test_score_user(score):
     if score < -0.6:
          return -1
     elif score > 0.6:
          return 1
     elif score > -0.1 and score < 0.1:
          return 0
     else:
          return None

def add_user(dic_score, dic, new_user, new_user_following, score):
     dic_score[new_user] = score
     for following in new_user_following:
          dic[following].append(new_user)

def calcul_sim(dic, new_user_following, user):
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

def score_prediction(dic_score, new_sim_dic):
     score = 0;
     denominateur = 0
     
     for user in dic_score:
          score += dic_score[user]*new_sim_dic[user]
          denominateur += abs(new_sim_dic[user])
     
     return score/denominateur

Path2 = "data.csv"
dic_score, dic = create_dic(Path)
unknown = convert_CSV_into_unknown(Path2)
main(dic, dic_score, unknown)

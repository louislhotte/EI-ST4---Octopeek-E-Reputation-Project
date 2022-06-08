import csv
import numpy as np
import pandas as pd


Path = ""
Unknown = []
Positive = []
Negative = []
Neutral = []

with open('eggs.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
          Unknown.append(row)

def create_follow(dataset):
     """
     :param dataset: Dataset avec les pseudos des individus labellisés "Pro-ElonMusk" et "Anti-ElonMusk", et les abonnements associés à la clé 'pseudo'
     :return: La matrice follow avec les individus labellisés en ligne, les abonnements en colonnes.
     Chaque indice follow[i][j] = 1 si l'individu i suit la page j, 0 sinon;
     Peut-être qu'un dictionnaire sera mieux adapté
     # Dic_score : {Pseudo : "Score"}
     # Dic = {Abonnement : "Pseudo"}
     """

     Pseudos = []
     #On va créer une liste de liste Pseudos, avec en Pseudo[i][0] = Pseudo et Pseudo[i][1] = 0, -1, 1
     # en fonction de sa positivité
     # Et Pseudo[i][2] va correspondre à la liste de ses abonnements

     # [A insérer, remplissage de Pseudos]

     Dic_score ={}
     Dic = {}
     n = len(Pseudos)
     for i in range(n):
          Dic_score[Pseudos[i][0]] = Pseudos[i][1]
          for x in Pseudos[i][2]:








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

     while len(Unknown) > 0 :
          follow = loop(Unknown)
          Compteur += 1

          # Si l'ordi n'arrive
          if Compteur > 100:
               break


     # Puis une fois qu'on a la matrice follow finale, il faut créer la matrice de similarité





     return


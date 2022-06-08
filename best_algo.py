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

def create_Sim(dataset):
     """
     :param dataset: Dataset avec les pseudos des individus labellisés "Pro-ElonMusk" et "Anti-ElonMusk", et les abonnements associés à la clé 'pseudo'
     :return: La matrice de similarité Sim avec les individus labellisés en ligne, les abonnements en colonnes.
     Chaque indice Sim[i][j] = 1 si l'individu i suit la page j, 0 sinon;
     Peut-être qu'un dictionnaire sera mieux adapté
     """
     

     Pseudos = []
     #On va créer une liste de liste Pseudos, avec en Pseudo[i][0] = Pseudo et Pseudo[i][1] = 0, -1, 1
     # en fonction de sa positivité
     # Et Pseudo[i][2] va correspondre à la liste de ses abonnements

     # [A insérer, remplissage de Pseudos]


     # Creation de la matrice Sim






def loop(Unkwown, Label):
     """
     :Input: Matrice de similarité remplie actuellement appelée "Sim", Liste Unknown, Matrice Label des pseudos labellisés "pour",
     "contre", ou "neutre" à propos d'Elon.
     :return: Matrice de similarité agrandie (avec les fortements positif, fortements neutre,
     fortement négatif rentrant dans la matrice), liste Unknown modifiée avec les pseudos qui sont
     entrés dans la matrice de similarité supprimés de Unknown
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
          Sim = loop(Unknown)
          Compteur += 1

          # Si l'ordi n'arrive
          if Compteur > 100:
               break

     # Puis une fois qu'on a la matrice de similarité, il faut classifier
     # dic_sim = similarity(Sim)



     return


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
     :param dataset: Dataset avec les pseudos des individus labellisés "Pro-ElonMusk" et "Anti-ElonMusk".
     :return: La matrice de similarité Sim avec les individus labellisés en ligne, les abonnements en colonnes.
     Chaque indice Sim[i][j] = 1 si l'individu i suit la page j, 0 sinon
     """
     

def loop(Sim, Unkwown, Label):
     """
     :Input: Matrice de similarité remplie actuellement appelée "Sim", Liste Unknown, Matrice Label des pseudos labellisés "pour",
     "contre", ou "neutre" à propos d'Elon.
     :return: Matrice de similarité agrandie (avec les fortements positif, fortements neutre,
     fortement négatif rentrant dans la matrice)
     """

     return


def main(Unknown, dataset):
     """
     :param: dataset (Dataset avec les pseudos des individus labellisés "Pro-ElonMusk" et "Anti-ElonMusk")
     Unknown (la liste des pseudos non 'classés')
     :return: Liste des
     """
     loop(list)
     return
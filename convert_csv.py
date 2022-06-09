import csv
CSV_path = "randomusers.csv"
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


                  dict[pseudo] = followers

     return dict


convert_CSV_into_unknown(CSV_path)
import csv

Pseudos = []
with open('datapart14.csv', newline='') as csvfile:
     read = csv.reader(csvfile)
     for row in read:
          if row != []:
               pseudo = row[0]
               print(pseudo)
               list = row[1][1:].split(', ')
               print(list)
               n = len(list)
               for i in range(len(list)-1):
                    list[i] = int(list[i])
               last_follower = int(list[n-1].split(']')[0])
               score = list[0]
               followers = list[1:n-2]
               followers.append(last_follower)
               print(followers)



# print(Pseudos)
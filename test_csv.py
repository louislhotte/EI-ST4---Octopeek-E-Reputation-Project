import csv

dic_score = {
    "elon_musks_hater": -1,
    "elon_musks_sucker": 1,
    "random_guy": 0
}

fieldname = []

for key in dic_score:
    fieldname.append(key)

with open('test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows([dic_score])
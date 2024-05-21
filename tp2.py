import json
import csv

with open('data.json', 'r') as json_file:
    nb_complexes = json.load(json_file)

csv_data = [["reel", "imaginaire"]]
for nb_complexes in nb_complexes:
    csv_data.append(nb_complexes)

with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)

print("Les nombres complexes sont maintenant dans data.csv")
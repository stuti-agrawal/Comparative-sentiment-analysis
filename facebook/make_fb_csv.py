import csv
import pandas as pd


# given a data text file and a label text file create a csv file
texts = []
sentiments = []
sentiments_map = {'O': 'negative', 'P': 'positive', 'N': 'neutral'}
count = 0
with open('fb_data.txt', 'r') as data_file:
    data = data_file.readlines()
    for line in data:
        texts.append(line.strip())

with open('C:/Users/stuti/Documents/CS410/Comparative-sentiment-analysis/facebook/fb_label.txt', 'r') as label_file:
    data = label_file.readlines()
    for line in data:
         # if line is empty, skip
        if not line.strip():
            continue
        
        # if length of line is 1, then it is the sentiment
        if len(line.strip()) == 1:
            sentiments.append(sentiments_map[line.strip()])

# create a csv file with the texts and sentiments
with open('facebook.csv', 'w', newline='') as csvfile:
    fieldnames = ['Text', 'Sentiment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(texts)):
        writer.writerow({'Text': texts[i], 'Sentiment': sentiments[i]})

# TODO: try again with punctuation 
import csv
import re

with open('../webscraping/talk_content.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # this is done to work with python types
    DATA = [""]
    for row in reader:
        for i in row:
            # data cleaning
            i = re.sub(".+?(?=talk)", "", i, count = 1)
            i = re.sub("talk", "", i, count = 1)
            i = re.sub("^[ \t]+", "", i)
            # make everything lowercase
            i = i.lower()
            # regex to keep uppercase:
            # i = re.sub("[^a-zA-Z' ]", "", i)
            # punctuation
            i = re.sub("[^a-z' ]", "", i)
            DATA.append(str(i))
# this is done to work with python types
DATA.pop(0)

print(len(DATA))
with open('cleaned_data.csv', 'w', encoding = 'UTF8', newline='\n') as f:
    writer = csv.writer(f)
    for i in range(0,len(DATA)-1):
        writer.writerow([DATA[i]])
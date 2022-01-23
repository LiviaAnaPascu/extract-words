import sys
import re
import csv
import glob
import enchant
from collections import Counter

conversationsDir = ""
files = glob.glob(f'{conversationsDir}*.txt')

def extract(input, username):
    spellcheck = enchant.Dict("en_GB")
    for input in files:
        with open(input, 'r', encoding='utf-8') as infile:
            listofwords = []
            for line in infile:
                if username in line:
                    text = line.split(':')[1]
                    [listofwords.append(word.strip().lower()) for word in re.findall('[a-zA-z]+', text) if spellcheck.check(word)]
    return listofwords

def toDict(input, username):
    listOfWords = extract(input, username)
    word =  Counter(listOfWords)
    resList = []
    for field in word:
        res = dict()
        res['Word'] = field
        res['Count'] = word[field]
        resList.append(res)
    return resList
    
def formatcsv(input, output, username):
    listdict= toDict(input, username)
    csv_columns = ['Word','Count']
    try:
        with open(output, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in listdict:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == "__main__":
    conversationsDir = str(sys.argv[0])
    username = str(sys.argv[1])
    output = str(sys.argv[2])
    formatcsv(files, f"{output}.csv", username)
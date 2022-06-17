import sys
import re
import csv
import enchant
import warnings
from glob import glob
from collections import Counter

def getChatFiles(conversationsDir):
    if not (conversationsDir and conversationsDir.strip()):
        warnings.warn("No working directory provided.")
    chatFiles = glob(f'{conversationsDir}/*.txt')
    if not chatFiles:
        warnings.warn("No conversations found at the current directory. ")
        print(conversationsDir)
    return chatFiles

def extract(conversationsDir, username):
    spellcheck = enchant.Dict("en_GB")
    chatFiles = getChatFiles(conversationsDir)
    listofwords = []
    for input in chatFiles:
        with open(input, 'r', encoding='utf-8') as infile:
            for line in infile:
                if not (username and username.strip()):
                    warnings.warn("No valid username provided.")
                elif isCorrectUsername(line, username):
                    text = line.split(':')[1]
                    [listofwords.append(word.strip().lower()) for word in re.findall('[a-zA-z]+', text) if spellcheck.check(word)]
    return listofwords

def isCorrectUsername(line, username):
    text = line.split(':')[0]
    if username in text:
        return True
    return False

def toDict(conversationsDir, username):
    listOfWords = extract(conversationsDir, username)
    word =  Counter(listOfWords)
    resList = []
    for field in word:
        res = dict()
        res['Word'] = field
        res['Count'] = word[field]
        res[username] = ""
        resList.append(res)
    return resList
    
def writeCSV(conversationsDir, output, username):
    listdict= toDict(conversationsDir, username)
    csv_columns = ['Word','Count', username]
    try:
        with open(output, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in listdict:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def main():
    conversationsDir = str(sys.argv[1])
    username = str(sys.argv[2])
    output = str(sys.argv[3])
    writeCSV(conversationsDir, f"{output}.csv", username)

if __name__ == "__main__":
    main()
# Andres Villasmil Ocando
# aev1@williams.edu
# Exam 1: File Search

import Epic
import os # need to get list of txt files

def findWord(word):
    newfiles = []
    for doc in os.listdir('.'):
        if doc.endswith('.txt'):
            newfiles.append(doc)
            
    count = 0
    dictionary = {}
    for doc in newfiles: 
        with open(doc, "r") as f:
            for line in f:
                for characters in line:
                    if count == len(word) - 1:
                        count = 0
                        dictionary.setdefault(doc, []).append(line)
                    elif word[count] == characters:
                        count = count + 1
                    else:
                        count = 0
                        continue
    return dictionary

def printWord(dictionary):
    for key in dictionary:
        for line in dictionary[key]:
            print(key + ":" + line)

def main():
    word = Epic.userStr("Enter word here:")
    dictionary = findWord(word)
    printWord(dictionary)
    
main()
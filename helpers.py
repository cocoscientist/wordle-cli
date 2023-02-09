#TODO: Function to fetch random word
import json
import random

def randomWord():
    with open('wordslist.json','r') as jsonList:
        mainList = json.load(jsonList)
        return random.choice(mainList)

def wordValidation(entered):
    return (len(entered)==5) and entered.isalpha()

def printChar(match, c):
    formatter = f"\033[{92+match}m"
    print(formatter + c + "\033[00m")
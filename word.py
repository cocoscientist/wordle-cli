from helpers import printChar, randomWord
import time

class Word:
    def __init__(self):
        #TODO: Select word randomly from a list
        self.word = randomWord()
        self.charset = set(self.word)

    def getWord(self):
        return self.word

    def compareWord(self,entered):
        matched = True
        entered = entered.upper()
        for i in range(5):
            if entered[i]==self.word[i]:
                printChar(0,entered[i])
            else:
                matched = False
                if entered[i] in self.charset:
                    printChar(1,entered[i])
                else:
                    print(entered[i])

            time.sleep(1.5)

        return matched

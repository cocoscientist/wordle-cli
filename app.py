from helpers import wordValidation
from word import Word

def mainloop():
    curWord = ''
    TRIES = 6
    WIN = False
    baseWord = Word()
    while TRIES>0 and not WIN:
        print("Tries Remaining:",TRIES)
        curWord = input("Enter your Word: ")
        while not wordValidation(curWord):
            print("Word entered incorrectly")
            curWord = input("Enter Word Again: ")

        WIN = baseWord.compareWord(curWord)
        TRIES -= 1
        if WIN:
            print("You win, Word is", curWord.lower(), "and you took", (6-TRIES), "tries")
        else:
            print("Try Again")
    
    if not WIN:
        print("You Lose!", "Word is", baseWord.getWord())


if __name__ == "__main__":
    print("Welcome to Wordle - CLI")
    mainloop()
from word import wordValidation

def mainloop():
    curWord = ''
    TRIES = 6
    WIN = False
    while TRIES>0 and not WIN:
        print("Tries Remaining:",TRIES)
        curWord = input("Enter your Word: ")
        while not wordValidation(curWord):
            print("Word entered incorrectly")
            curWord = input("Enter Word Again: ")
        
        print(curWord)
        TRIES -= 1


if __name__ == "__main__":
    print("Welcome to Wordle - CLI")
    mainloop()
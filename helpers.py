def wordValidation(entered):
    return (len(entered)==5) and entered.isalpha()

def printChar(match, c):
    formatter = f"\033[{92+match}m"
    print(formatter + c + "\033[00m")
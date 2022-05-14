inputNumber = int(input("Enter Number to get a pattern "))

def patternAsterisk(inputNumber):
    lineNumber = 0
    for i in range(0, inputNumber*inputNumber*2):
        if i%(inputNumber*2) == 0:
            print()
            lineNumber += 1
            printStar(lineNumber, inputNumber)

def printStar(lineNumber, inputNumber):
    if lineNumber%2 == 0:    
        for i in range(0, inputNumber*2):
            if i%2 == 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    # Even line
    else:
        for i in range(0, inputNumber*2):
            if i%2 != 0:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    # Odd line

patternAsterisk(inputNumber)
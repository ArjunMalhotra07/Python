inputNumber = eval(input("Enter a Number to find its factorial "))

def factorial(inputNumber):
    if inputNumber == 1:
        return inputNumber
    return inputNumber * factorial(inputNumber-1)

print("Factorial of Given Number ",factorial(inputNumber))
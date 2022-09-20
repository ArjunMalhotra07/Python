a = eval(input("Enter Number "))

def primeOrNot(testNumber):
    flag = True
    for i in range (2,testNumber//2):
        if (testNumber%i) == 0:
            print(testNumber, " Not Prime")
            flag = False
            return flag
    if flag == True:
        print(testNumber, "Prime")
        return flag

finalAns = primeOrNot(a)

if finalAns == False:
    for i in range(a-1, a//2, -1):
        if primeOrNot(i) == True:
            break

    for i in range(a+1, a+a//2, +1):
        if primeOrNot(i) == True:
            break
        else:
            continue






 
    

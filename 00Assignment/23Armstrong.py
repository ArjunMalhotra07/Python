number=eval(input("Enter Number to Check if Armstrong or Not "))
testNumber = number
sum = 0
while(testNumber>0):
    rem = testNumber%10
    testNumber = testNumber//10
    sum += rem*rem*rem

if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")

binaryNum = eval(input("Enter number to get its binary "))


def binaryNumber(binaryNum):
    sum = 0
    binaryList = []
    while binaryNum > 0:
        rem = binaryNum%2
        binaryNum //= 2
        binaryList.append(rem)

    for i in range(len(binaryList)-1, -1, -1):
        sum = sum*10 + binaryList[i]
    if (sum<1000 and  sum>=100):
        print("Binary Form : 0%d"%sum)
    elif (sum<100 and  sum>=10):
        print("Binary Form : 00%d"%sum)
    elif (sum<10 and  sum>=0):
        print("Binary Form : 000%d"%sum)
    else:
        print("Binary Form : ",sum)
     

binaryNumber(binaryNum)

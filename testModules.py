def sumOfApSeries(n,a,d):
    nBytwo = int(n/2)
    twoA = 2*a
    nMinusOneintoD = (n-1)*d
    return nBytwo * (twoA + nMinusOneintoD)
    
    
def sumOfList(listOfNumbers):
    sum = 0
    for i in range(0, len(listOfNumbers)):
        sum += listOfNumbers[i]
    return sum

def sortList(listOfNumbers):
    for i in range (0, len(listOfNumbers)):
        for j in range(0 , len(listOfNumbers)-i-1):
            if listOfNumbers[j] > listOfNumbers[j+1]:
                listOfNumbers[j] , listOfNumbers[j+1] = listOfNumbers[j+1] , listOfNumbers[j]

    return(listOfNumbers)
testString = "madam "

def everySubstring(testString):
    length = len(testString)
    allSubstrings = []
    for j in range (1, length+1):
        step = j
        for i in range (0, length-1):
            start = i
            end = start + step + 1 
            if end <= length:
                allSubstrings.append(testString[start:end])
    return(allSubstrings)
    
ansArray = everySubstring(testString)
print("All Substrings : ", ansArray)

print()

def palindrome(ansArray):
    newAnsArray = []
    lengthArray = len(ansArray)
    for i in range (0, lengthArray):
        reversedString = ""
        testWord = ansArray[i]
        for j in range (len(testWord)-1, -1, -1):
            reversedString += testWord[j]

        if reversedString == testWord:
            newAnsArray.append(reversedString)
    return newAnsArray

print("Palindromic Substrings : ", palindrome(ansArray))
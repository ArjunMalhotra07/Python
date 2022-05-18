inString = "arjun"

dictionaryMap = {}
count = 0
last = inString[len(inString)-1]

for i in range (0, len(inString)-1):
    if inString[i] not in dictionaryMap:
        for j in range (i+1, len(inString)):
                if inString[i] == inString[j]:
                    count += 1  
        dictionaryMap[inString[i]] = count + 1
        count = 0

if last not in dictionaryMap:
    dictionaryMap[last] = 1

print(dictionaryMap)

errCount = 0
for key, val in dictionaryMap.items():
    if val % 2 != 0:
        errLetter = key
        errCount += 1


if errCount==1 :
    print("String can be made Palindrome ")
else:
    print("String cannot be made Palindrome ")





        


   



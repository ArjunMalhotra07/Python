inString = "arjun"

dictionary = {}
count = 1
last = inString[len(inString)-1]

for i in range (0, len(inString)-1):
    for j in range (1, len(inString)):
        if inString[i] in dictionary:
            continue
        else:
            if inString[i] == inString[j]:
                count += 1  
    dictionary[inString[i]] = count
    count = 0

if last not in dictionary:
    dictionary[last] = 1

print(dictionary)



   



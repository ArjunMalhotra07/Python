nameList = []
for i in range(0,5):
    print("Enter Name " , i+1 , end = " ")
    inputName = input()
    nameList.append(inputName)

print("Original List : ",nameList)

namesWithEep = []
for i in range(0, len(nameList)):
    if "eep" in nameList[i]:
        namesWithEep.append(nameList[i])

print("Answer List : ",namesWithEep)

    
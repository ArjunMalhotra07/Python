list1 = [5,6,7]
list2 = [25,49,36, 57]

iFlag = False
for i in range (0, len(list1)):
    jFlag = False

    for j in range (0, len(list2)):
        if list1[i]*list1[i] == list2[j]:
            jFlag = True
            break

    if jFlag == False:
        iFlag = False
        break
    else:
        iFlag = True

if iFlag == True:
    print("true")
else:
    print("Not true")
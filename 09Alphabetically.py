print ("names")
list1=[]
for i in range (0,5):
    names=input()
    list1.append(names)
print (list1)

def order(word1, word2):
    list1 = []
    for i in range(0, len(word1)):
        list1.append(ord(word1[i]))
    # print(list1)

    list2 = []
    for j in range(0, len(word2)):
        list2.append(ord(word2[j]))
    # print(list2)
    
    length = 0
    length1 = len(word1)
    length2 = len(word2)
    if length1 > length2:
        length = length2
    else:
        length = length1

    for i in range(0, length):
        if list1[i]!= list2[i]:
            return i


for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-i-1):
        temp1=list1[j]  
        temp2=list1[j+1]
        # print(temp1, temp2)
        index = order(temp1, temp2)

        subString1 = temp1[index]
        subString2 = temp2[index]

        if ord(subString1) > ord (subString2):
            list1[j],list1[j+1]=list1[j+1],list1[j]

print(list1)
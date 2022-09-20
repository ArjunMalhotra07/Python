print ("Enter 5 Names : ")
list1=[]
for i in range (0,5):
    print(i+1, end=" : ")
    names=input()
    list1.append(names)
print ("Entered List : ",list1)

# Function to return the index of comparison between 2 Names
def order(word1, word2):
    list1 = []
    for i in range(0, len(word1)):
        list1.append(ord(word1[i]))

    list2 = []
    for j in range(0, len(word2)):
        list2.append(ord(word2[j]))
    
    length1 = len(word1)
    length2 = len(word2)
    if length1 > length2:
        length = length2
    else:
        length = length1

    for i in range(0, length):
        if list1[i]!= list2[i]:
            return i

# loop to Sort List By Names
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-i-1):
        name1=list1[j]  
        name2=list1[j+1]
        index = order(name1, name2)
        if index!= None:
            character1 = name1[index]
            character2 = name2[index]
            if ord(character1) > ord (character2):
                list1[j],list1[j+1]=list1[j+1],list1[j]
        else:
            if len(name1) > len(name2):
                list1[j],list1[j+1]=list1[j+1],list1[j]

print("Alphabetically",list1)
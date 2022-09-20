list1 = ['a','z','y','b']

for i in range(0, len(list1)-1):
    for j in range(0, len(list1)-i-1):
        tempAscii1 = ord(list1[j])
        tempAscii2 = ord(list1[j+1])
        if tempAscii1 < tempAscii2:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)


list2 = [5,10,1,-8,48,500,265]

for i in range (0, len(list2)-1):
    for j in range(0, len(list2)-1-i):
        if list2[j] > list2[j+1]:
            list2[j] , list2[j+1] = list2[j+1] , list2[j]

print(list2)
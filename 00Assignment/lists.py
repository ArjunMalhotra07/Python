print()
length = eval(input(" Enter the length of 2 Lists here - "))

def enterList (length):
    arr = []
    for i in range(0 , length):
        print(i+1, end = " : ")
        number = eval(input())
        arr.append(number)
    return arr
        
arr1 = enterList(length)
print()
print("List 1 : ",arr1)
print()
arr2 = enterList(length)
print("List 2 : ",arr2)
print()

def checkEqual( arr1, arr2, length):
    for i in range(0, length):
        flag = False
        for j in range(0, length):
            if arr1[i] == arr2[j]:  
                flag = True
                break
        if flag == False:
            print("Not Equal")
            break
        else:
            continue
    if flag != False:
        print("Equal")

checkEqual(arr1, arr2, length)
print(" Enter 5 Numbers ")
print()
arr = []
for i in range(0 , 5):
    number = eval(input(" Enter Number "))
    arr.append(number)
print()
print("Entered list : ",arr)


for i in range(0 , len(arr)-1):
    for j in range(0 , len(arr)-i-1):
        if arr[j] < arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
print()
print("Sorted List : ",arr)

numbers = [15,20,25,30,65,89]
searchNumber = eval(input("Enter a Number "))

flag = False
for i in range (0,len(numbers)):
    if numbers[i]== searchNumber:
        flag = True
        print("Found at Index ",i)

if flag == False:
    print("Not found")
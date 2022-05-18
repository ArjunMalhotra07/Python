rows  = eval(input (" Enter rows "))
m = rows - 1
n = 0
for i in range(0,rows):

    for j in range (m,-1, -1):
        print(end = " ")          #  Triangle
        # print(" ",end = " ")    # Right Tri

    for k in range (0, n+1 ):
        print("*", end = " ")

    print()
    m -= 1
    n += 1




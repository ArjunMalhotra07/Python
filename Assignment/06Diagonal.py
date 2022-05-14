matrix1 = [[1,2,33],[44,26,35],[77,8,9]]
for i in range(0, len(matrix1)):
    print (matrix1[i])

sum = 0
flag = True
for i in range (0,len(matrix1)):
    rows = len(matrix1)
    columns = len(matrix1[i])
    if rows == columns:
        sum+= matrix1[i][i]
    else:
        flag = False
        print("Diagonal Sum not possible ")
        break
if flag == True:
    print("Sum of Diagonal Elements ",sum)

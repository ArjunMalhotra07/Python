matrix1 = [[15,16,19],[102,105,78],[989,56,7]]
sum = 0 
for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1[i])):
        sum += matrix1[i][j]

print(sum)
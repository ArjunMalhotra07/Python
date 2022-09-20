matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[11,22,33],[44,55,66],[77,88,99]]


def printMatrix(incomingMatrix):
    for i in range(0, len(incomingMatrix)):
        print (incomingMatrix[i])
    

printMatrix(matrix1)
print()
printMatrix(matrix2)
print()

for i in range (0,len(matrix1)):
    for j in range (0, len(matrix1[0])):
        matrix1[i][j]+= matrix2[i][j]

print("Addition -- ")
print()
printMatrix(matrix1)

prime = []
non_Prime = []
a = eval(input("Enter a "))
b = eval(input("Enter b "))
for i in range (a, b):
    for j in range(2, i):
        if i%j ==0:
            non_Prime.append(i)
            break
    else:
        prime.append(i)
print("Prime Numbers between ", a, " and ", b, prime)
print("Non-Prime Numbers between ",a, " and ", b, non_Prime)

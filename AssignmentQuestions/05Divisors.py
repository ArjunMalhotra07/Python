num = eval(input("Enter number to get its diviors "))

divisors = []

for i in range(2,num//2+1):
    if num%i == 0:
        divisors.append(i)

divisors.append(1)
divisors.append(num)
print(divisors)

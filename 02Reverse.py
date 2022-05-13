a= eval(input("Enter 4 digit number "))
b = a
if a>=1000 and a<=9999 :
    print(a, " is 4 digit number")
else:
    print("Not a 4 digit number")

reverse = 0
while a!=0 :
    mod = a % 10
    reverse = reverse*10 + mod 
    a //= 10
print ("Reverse ",reverse)

sum=0
while b!=0 :
    mod = b % 10
    sum += mod 
    b //= 10
print ("Sum ",sum)


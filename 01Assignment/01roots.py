import math

a= float(input("Enter A "))
b= float(input("Enter B "))
c= float(input("Enter C "))
print(a)
print(b)
print(c)

if a == 0:
    print("Error a=0 cannot be ")
else:
    d = (b*b) - (4*a*c)
    if d >= 0:
        sqRoot = math.sqrt((b*b) - (4*a*c))
        root1 = (-b + sqRoot)/2*a
        root2 = (-b - sqRoot)/2*a
        print("Roots : ",root1, root2)
    else:
        print("Imaginary Roots")
    




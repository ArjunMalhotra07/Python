f = open('test.txt','rb')
print(f)

print(f.readline())
print(f.readline())
f.close()

f1 = open('test.txt','a')
f1.write("nipun")
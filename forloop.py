list = ["shailendra"]
for char in list:
    print(char)

l = [1,4,16,36,64,124,144]
for i in l:
    print(i)
x = 64
inx=0
for i in l:
    if(x==i):
        print("found at index : ",inx)
    inx+=1  

l = [1,2,3,4,56,68]
for i in range(0,5,1):
    print(i)

l = [1,2,3,4,56,68]
for i in range(2,10,5):
    print(i)

n = 6

for i in range(1,11,1):
    a = i*n
    print(f"{n} * {i} = {a}")
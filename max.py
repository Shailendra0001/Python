l = [23,14,35,56]
max = 0
index = 0
for i in range (len(l)):
    if(max<l[i]):
        max = l[i]
        index = i
print(f"greatest number is list is {max} and index is {index}",)
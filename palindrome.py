s = input("enter : ")
b = ""
for i in range(len(s)-1,-1,-1):
    b = b + s[i]

if b == s:
    print("it is a palindrome")
else:
        print("it is not a palindrome")
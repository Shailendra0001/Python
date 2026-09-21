n = int(input("enter number : "))
perfect = 0
for i in range (1,n):
    if n%i==0:
        perfect += i
if perfect == n:
   print(f"entered number is a perfect number") 
def num(n):
    if(n==0):
        return
    print(n)
    num(n-1)
 
num(5)

def fact(n):
    
    if(n==0 or n==1):
        return 1
    else : 
        return n * fact(n-1)
a = fact(  4)
print(a)

def sum_upto(n):
    if(n==0):
        return 0
    return n + sum_upto(n-1)
 
print(sum_upto(10))

l=[1,2,3,4,5]
def list(l,i):
    if(i==0):
        return
    else:
        print(i)

list(l,4)
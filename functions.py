def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(1,2)
calc_sum(3,5) 

l = ["iron man ", "superman" , "hehheeh"]
def list(l):
    for i in l:
        print(i, end="")
list(l)

def factorial(n):
    fact = 1 
    for i in range(1,n+1):
        fact = fact * i
    print (fact)

factorial(4)

def convert(u):
    i = u * 83
    print(u,'USD =', i, "INR")
convert(1)

def check(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

check(19)
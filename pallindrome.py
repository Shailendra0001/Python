def is_number_palindrome(n):
    if n<0:
        return False
    orignal = n
    reversed_num = 0

    while n>0:
        digit = n%10
        reversed_num=(reversed_num*10) + digit
        n= n//10
    return orignal==reversed_num

print(is_number_palindrome(1221))
print(is_number_palindrome(-121))
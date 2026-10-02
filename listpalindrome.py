list1 = [1,2,3,4]
list1.copy()
list2 = list1.copy()
list2.reverse()
if(list2==list1):
    print("palindrome")
else:
    print("not a palindrome")
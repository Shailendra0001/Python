passw = input("enter password : ")
if(len(passw)==8 and passw[0].isupper() and not any(ch.isdigit() for ch in passw and " " not in passw)):
    print("valid passowrd")
else:
    print("invalid password")
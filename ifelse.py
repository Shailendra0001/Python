age = int(input("enter your age :"))
own_car = input("enter true or false :")
if(age>=18):
    if(own_car=="true"):
        print("you can drive")
    else:
        print("you cant drive")
else:
    print("work hard and buy ur car")
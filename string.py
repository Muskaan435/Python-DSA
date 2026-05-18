# val = [i*i for i in range(1,11)]
# print(val)

# a,b=[int(x) for x in input("Enter 2 numbers : ").split()]
# print("product is : ",a*b)

# a,b,c=[float(x) for x in input("Enter 3 float numbers : ").split(',')]
# print("Sum is : ",a+b+c)

# myCart = [10,20,800,60,70]
# for item in myCart:
#     if item>400:
#         print("this is not in my budget")
#         continue
#     else:
#         print(item)


while(True):
    uname = input("Enter username : ")
    passw = input("enter password : ")
    if uname == "admin" and passw == "admin":
        print("Login sucess")
        break
    else:
        print("Login Failed")
# why python is called dynamically typed language?

# age = 22
# pi = 3.14
# Name = "Muskan"
# result = True

# print(type(age))
# print(type(pi))
# print(type(Name))
# print(type(result))

# print(id(age))
# print(id(pi))
# print(id(Name))
# print(id(result))

# print(2+2)
# print("2"+"2")
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print(a+b) 

# print(int(3.74))
# print(int(True))
# print(int(False))
# print(int("123"))
# print(int("3.14")) # This will raise an error because "3.14" is not a valid integer string
# print(int(10+5j)) # This will raise an error because complex numbers cannot be converted to integers
# print(int("muskan")) # This will raise an error because "muskan" is not a valid integer string

# print(float(3))
# print(float(True))
# print(float(False))
# print(float(3.14))
# print(float("3.14"))
# print(float("123"))
# print(float("muskan")) # This will raise an error because "muskan" is not a valid float string
# print(float(10+5j)) # This will raise an error because complex numbers cannot be converted to floats

# complex() eswd to convert

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(5,-3))
# print(complex(True, False))

#bool() is used to convert a value to a boolean (True or False)

# print(bool(0)) 
# print(bool(1)) 
# print(bool(-1)) 
# print(bool(0.0)) 
# print(bool(0.1)) 
# print(bool("")) 
# print(bool(" ")) 
# print(bool("False"))  
# print(bool(True)) 
# print(bool(0+0j)) 
# print(bool(1+2j)) 

# simple if
# a = int(input("Enter any single digit: "))
# if a>0:
#     print("The number is positive.")
# elif a<0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


# using if-else take input from user in both upper and lower case and print that the day is weekday or weekend

# day = input("Enter the day of the week: ")
# if day == "saturday" or day == "sunday" or day == "SUNDAY" or day == "SATURDAY":
#     print("The day is a weekend.")
# else:
#     print("The day is a Working day.")

# else if ladder

# per = 65

# if per >=65:
#     print("Grade A")
# elif per<=65 and per >=50:
#     print("Grade B")
# else:
#     print("Fail")

# ORD converts the value into ascii code

# chr = ord(input("Enter any one character : "))
# if chr >=65 and chr<=90:
#     print("Upper case")
# elif chr >=97 and chr<=122:
#     print("Lower case")
# elif chr >=48 and chr<=57:
#     print("Digit")
# else:
#     print("Special character")

# membership operator

# name = "MuskanDeepakPichhode"
# print("z" in name)
# print("M" not in name)

# Identity operator is used to check if two variables refer to the same object in memory

# a = 10
# b = 10
# print(a is b) # True, because small integers are cached by Python
# print(a is not b) # False, because a and b refer to the same object in memory

# for i in range(2,10,2):
#     print(i) 

# print table from 2-20  using for loop
 
# for i in range (1,11):
#     print(i * 2 , "  " ,i*3 ,"  " ,i*4 , "  ", i*5 , "  ", i*6 , "  " ,i*7 , "  ", i*8 ,"  " ,i*9 , "  " ,i*10 )

# print("----------------------------------------------------------------------------------")

# for i in range (1,11):
#     print(i * 11, "  " ,i*12 ,"  " ,i*13 , "  ", i*14 , "  ", i*15 , "  " ,i*16 , "  ", i*17 ,"  " ,i*18 , "  " ,i*19 , "  ", i*20)

# marks1 = int(input("Enter marks for subject1 : "))
# marks2 = int(input("Enter marks for subject2 : "))
# marks3 = int(input("Enter marks for subject3 : "))
# gender = input("Enter your gender (M/F) : ").lower()

# total = marks1+marks2+marks3
# print("Total marks : ",total)
# per = (total/300) *100
# print("Percentage : ",per)
# if marks3 >= 35 and marks2 >= 35 and marks1 >= 35:
#     print("PASS")
# else:
#     print("Fail")

# if per >= 65 and gender == "m":
#     print("You are eligible for placements")
# else:
#     print("You are not eligible for placements")


for i in range (1,6):
    high = 6 - i

    if i == 3 or high == 3:
        continue

    print(i , "  ", high)

# zip() we can take multiple range function inside zip()

for i,j in zip(range(1,6), range(5,0,-1)):
    if i == 3 and j == 3:
        continue
    print(i , "  ", j)
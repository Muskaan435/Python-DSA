#  name="MuskanPichodeMCAstudent"

# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


# s = "python are High level programming language"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.swapcase())
# print(s.title())

# name = "prashant"
# sal = 5000
# age = 25

# print("{} salary is {} and age is {}".format(name, sal, age))
# print("{0} salary is {1} and age is {2}".format(name, sal, age))
# print("{x} salary is {y} and age is {z}".format(x=name, y=sal, z=age))
# A = 1
# print(f"{A} is a good boy")

# remove duplicate characters from the string
# name = "Muskaan"
# newName=""
# for i in name:
#     if i not in newName:
#         newName+=i

# print(newName)

# write a program to reverse the string
# name="pichhode"
# newname=""
# n = name.length()

# for i in range(n-1, -1, -1):
#     newname+=name[i]

# print(newname)

# write a program to check whether the given string is palindrome or not
# name = "kanak"
# newname=""

# for i in range(len(name)-1, -1, -1):
#     newname+=name[i]

# if name == newname:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# write a program to count number of vovels and consonants in the string
# name = "muskanPichhode"
# name = name.lower()
# vovels = 0
# consonants = 0

# for i in name:
#     if i in "aeiou":
#         vovels+=1
#     else:
#         consonants+=1

# print("Vovels: ", vovels, "Consonants: ", consonants)        

# write a program to check anagram or not

# name1 = "listens"
# name2 = "silent"
# name1 = name1.lower()
# name2 = name2.lower()

# if sorted(name1) == sorted(name2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# count number of words in the string
# string = "python is a programming language"
# words = 1

# for i in string:
#     if i == " ":
#         words+=1

# print(words)

# a = 50
# b=30
# c=20
# d=10

# print((a+b)*c/d)
# print((a-b)*c/d)
# print((a*b)*c/d)

# input
# n = "gasgg54@#vssd!s*"
# spschr = 0
# for char in n:
#     if char in ["@", "#", "!", "*"]:
#         spschr+=1

# print("Number of special characters: ", spschr)
        
# print("muskanpichode04".isalnum())
# print("muskanpichode".isalpha())
# print("123456f".isdigit())
# print("muskanpichode".islower())
# print("MUSKANPICHOdE".isupper())
# print("My Name Is Muskan".istitle())
# print("".isspace())
# print("".istitle())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

# print("Hello World".find("o"))
# print("Hello World".index("o"))
# print("Hello World".count("o"))

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# n = int(input("Enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(chr(64+i), end=" ")
#     print()


# n = int(input("Enter the number of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("*", end=" ")
#     print()

# import time
# n = int(input("Enter the number of rows : "))
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         print("* ", end="")
#         time.sleep(0.5)
#     print()


# tuplesss

# mytuple = ("Muskan", "Pichhode", 20, 5000, "MCA Student","rahul", "sandip")
# print(mytuple)
# print(type(mytuple))

# mytuple[2] = "pichode"
# print(mytuple)

# init_tuple =()
# print(init_tuple.__len__()) # 0 because there are no elements in the tuple so length is 0

# init_tuple_a = 'a','b'
# init_tuple_b = ('a','b')
# print(init_tuple_a == init_tuple_b) # True because both are tuples and have same elements

# init_tuple_a = '1','2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b) # ('1','2','3','4') because + operator concatenates the two tuples and creates a new tuple with all the elements of both tuples

# l = [1,2,3]
# init_tuple = ('python',) * (l.__len__() - l[::-1][0])
# print(init_tuple) # because l.__len__() is 3 and l[::-1][0] is 3 so 3-3 is 0 and 'python' * 0 is '' so the output is an empty tuple ()

# init_tuple = ('python') * 3
# print(type(init_tuple)) # because 'python' * 3 is 'pythonpythonpython' 

# init_tuple = ((1,2),) *7
# print(len(init_tuple[3:8])) # because init_tuple[3:8] is ((1,2), (1,2), (1,2), (1,2)) so the length of this tuple is 4

# mydict = {101:"muskan",
#           102:"pichhode",
#           103:"mca student",
#           104:"rahul",
#           105:"sandip",
#          }

# print(mydict) # because in a dictionary keys are unique so when we try to add a key that already exists it will update the value of that key instead of adding a new key-value pair so the output will be {101: 'muskaan', 102: 'pichhode', 103: 'mca student', 104: 'pichhode', 105: 'sandip'}

# num = 123456
# a = num% 10 #6
# num = num //10
# b = num% 10 #5
# num = num // 10
# c = num% 10 #4
# num = num // 10
# d = num % 10 #3
# num = num // 10
# e = num % 10 #2
# f = num//10 #1

# rev = a*100000 + b*10000 + c *1000 + d*100 + e*10 + f
# print(rev)

# Amount = int(input("Enter the amount to be withdrawn : "))

# print("100 rs notes : ", Amount // 100)
# print("50 rs notes : ", (Amount % 100) // 50)
# print("20 rs notes : ",((Amount % 100) % 50) // 20)
# print("10 rs notes : ",(((Amount % 100) % 50)%20) // 10)
# print("5 rs notes : ",((((Amount % 100) % 50)%20)%10) // 5)
# print("2 rs notes : ",(((((Amount % 100) % 50)%20)%10)%5) // 2)
# print("1 rs notes : ",((((((Amount % 100) % 50)%20)%10)%5)%2) // 1)

# maximum consecutive ones in a binary number
# ls = [1,1,0,1,1,1,0,1,1,1,1]

# count = 0
# max_count = 0

# for i in ls:
#     if i == 1:
#         count+=1
#     else:
#         max_count = max(max_count, count)
#         count = 0

# print(max(max_count, count))

# count substring in a string

# string = "abababab"
# substring = "ab"
# count = 0

# for i in range(len(string)-len(substring)+1):
#     if string[i:i+len(substring)] == substring:
#         count+=1

# print(count)

# i = 1
# while i<=5:
#     print(i)
#     i+=1

# def arithmatic():
#     a = int(input("enter the value of A :"))
#     b = int(input("enter the value of B : "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul

# print(arithmatic())


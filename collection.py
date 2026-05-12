
list = [0,1,4,0,2,5]

for i in list:
    if i == 0:
        del list[i]
        list.append(0)

print(list)


# mylist = ["prashant", "Komal","Ankush","Ashish",77,"Sandip",60.52,"Muskan"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# mylist[2] = "akshay"
# if "Komal" in mylist:
#     print("Komal is in the list")
# else:
#     print("Komal is not in the list")

# mylist.append("Mona")
# mylist.append("Pichhode")
# mylist.insert(2,"Akshay")


# mylist.remove("Sandip")
# newlist = mylist.copy()
# print(newlist)

# newlist = [['prashant','jha'],['85.56'],[440022,'yyy']]

# print("example of multidimensional list")
# print(newlist)
# print(newlist[0][0])
# print(newlist[0][1])
# print(newlist[1][0])
# print(newlist[2][0])
# print(newlist[2][1])

# list2 = [50,25.50,"prashant"]
# del list2
# print(list2)

# name = "prashant"
# print(name)
# myname = list(name)
# print(myname)

# mylist = [44,22,77,0,9,88]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)

# default sorting order for numbers is ascending order for string it is alphabetical order we should know that list should contain homogeneous data type otherwise it will raise an error while sorting

# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# for i in mylist:
#     print(i)
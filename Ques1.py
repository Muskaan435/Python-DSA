# Questions Day 1
# second largest element in the list
# arr = [7,3,9,2,8]

# arr.sort(reverse=True)
# print(arr[1])

# Question 2
# predict output of the above code

# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a)

# Question 3
# predict output of the below code

# a= [1,2,3,4,5]
# print(a[3:0:-1])

# Question 4
# predict output of the below code

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]

# for i in range(0,4):
#     print(arr[i].pop())

# Question 5
# predict output of the below code
# arr = [1,2,3,4,5,6] 

# for i in range(0,6):
#     arr[i -1] = arr[i]

# for i in range(0,6):
#     print(arr[i], end="  ")


# question 6
# predict output of the below code

# fruit_List1 = ["apple", "berry", "cherry","Papaya"]
# fruit_list2 = fruit_List1
# fruit_list3 = fruit_List1[:]
# fruit_list2[0] = "Guava"
# fruit_list3[1] = "Kiwi"

# sum = 0
# for ls in (fruit_List1, fruit_list2, fruit_list3):
#     if ls[0] == "Guava":
#         sum+= 1
#     if ls[1] == "Kiwi":
#         sum+= 20

# print(sum)

# Question 7

mylist=[]
N =int(input("Enter the value of N : "))
for i in range(N):
    val = int(input("Enter a number : "))
    mylist.append(val)
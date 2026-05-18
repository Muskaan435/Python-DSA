# # Queue DS:-
# # 1. EnQueue
# # 2. DeQueue
# # 3. Display Queue
# # 4. Peek Operation
# # 5. Delete Queue
# # 6. Exit

# import sys

# class Queue:
#     def __init__(self, size):
#         self.myQueue = []   # Creating Queue
#         self.queueSize = size   # Queue size defined

#     def isFull(self):
#         if len(self.myQueue) == self.queueSize:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if len(self.myQueue) == 0:
#             return True
#         else:
#             return False

#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full! Cannot Insert.")
#         else:
#             self.myQueue.append(value)
#             print(value, "Inserted Successfully.")

#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty! Cannot Delete.")
#         else:
#             deleted = self.myQueue.pop(0)
#             print(deleted, "Deleted Successfully.")

#     def displayQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty!")
#         else:
#             print("Queue Elements are :", self.myQueue)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty!")
#         else:
#             print("Front Element is :", self.myQueue[0])

#     def deleteQueue(self):
#         self.myQueue.clear()
#         print("Queue Deleted Successfully.")


# # Main Program
# size = int(input("Enter the Size of Queue : "))
# obj = Queue(size)

# print("Queue has Created : ")

# while True:
#     print("\n====================== Queue ======================")
#     print("1. EnQueue Operation")
#     print("2. DeQueue Operation")
#     print("3. Display Queue")
#     print("4. Peek Operation")
#     print("5. Delete Queue")
#     print("6. Exit")
#     print("===================================================")

#     choice = int(input("Enter Your Choice : "))

#     if choice == 1:
#         value = int(input("Enter Value to Insert : "))
#         obj.enQueue(value)

#     elif choice == 2:
#         obj.deQueue()

#     elif choice == 3:
#         obj.displayQueue()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteQueue()

#     elif choice == 6:
#         print("Program Exit...")
#         sys.exit()

#     else:
#         print("Invalid Choice! Please Try Again.")

# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] +=1
#     else:
#         fruit[index] = 1
# addone("apple")
# addone("banana")
# addone("Apple")

# print(len(fruit))

students= {}
def addstu(index,marks):
    if index in students:
        students[index] = marks
    else:
        students[index] = marks

def displaystu(name):
    for i in range(len(students)):
        


addstu("muskan",65)
addstu("khushi",77)
addstu("karti",88)

print(students)


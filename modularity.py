import sys
def add():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a + b)

def sub():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a - b)

def mul():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a * b)

def div():
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    print(a / b)


while(True):
    print("1. Addition")
    print("2. Subtration")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    else:
        sys.exit()
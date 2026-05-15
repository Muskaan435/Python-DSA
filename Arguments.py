# positional argument

def add(a,b):
    return a+b

print(add(5,5))

# keyword argument

def credential(username,password):
    if(username == password):
        print("success login")   
    else:
        print("Sucess Denied") 
        
credential(username="admin",password="admin")

# default argument 

def default(name="Muskan"):
    print(name)

default("karti")
default()

# variable length

def varlength(*city):
    print(city)

varlength("Nagpur", "Mumbai","lonavala")

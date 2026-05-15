# remove spacing from the string
# rstrip() => to remove space from the right hand side
# lstrip() => to remove space from the left hand side
# strip() => to remove space from both side



city=input("Enter your city Name : ")
scity = city.strip()

if scity == "Hydrabad":
    print("Hello Hydrabadi..Adab")
elif scity == "Chennai":
    print("Hello Madrasi..Wadakkam")
elif scity == "Banglore":
    print("Hello kannadiga..shubhogaya")
else:
    print("your Entered city is invalid")

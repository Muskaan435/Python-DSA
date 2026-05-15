string = "muskan*is*a*good*programmer"
newname = ""
val = ""

for i in string:
    if i == "*":
        val +=i
    else:
        newname +=i

print(newname)
print(str(val+newname))
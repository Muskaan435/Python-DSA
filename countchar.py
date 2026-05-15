char = "aabbbbccceeeee"
newname = {}
for i in range(len(char)):
    key = char[i]
    count = 0
    for j in range(len(char)):
        if key == char[j]:
            count+=1
    newname[key] = count

for i, j in newname.items():
    print(i,j,sep= '',end="")
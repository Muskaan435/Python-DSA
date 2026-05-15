# max in row
list = [[100,198,333,323],
        [122,232,221,111],
        [223,565,245,764]]

for i in range(0,len(list)):
    max = list[i][0]

    for j in range(1,len(list[i])):
        if(list[i][j] > max):
            max = list[i][j]
        
    print(max)

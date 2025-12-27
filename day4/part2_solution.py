with open('day4/input.txt', 'r') as file:
    
    arr2d = [list(line.strip()) for line in file]
    toRemove = []
    accessibleRolls = 0
    while 1==1:
        for i in range(len(arr2d)):
            for j in range(len(arr2d[i])):
                adjRolls = 0
                if(arr2d[i][j] != "@"): continue
                if(j-1 >= 0):
                    if(arr2d[i][j-1] == "@"): adjRolls += 1
                    if(i-1 >= 0):
                        if(arr2d[i-1][j-1] == "@"): adjRolls += 1
                if(i-1>=0):
                    if(arr2d[i-1][j] == "@"): adjRolls += 1
                    if(j+1<len(arr2d[i])):
                        if(arr2d[i-1][j+1] == "@"): adjRolls += 1

                if(j+1<len(arr2d[i])):              
                    if(arr2d[i][j+1] == "@"): adjRolls += 1
                    if(i+1 < len(arr2d)):
                        if(arr2d[i+1][j+1] == "@"): adjRolls += 1
                if(i+1<len(arr2d)):
                    if(arr2d[i+1][j] == "@"): adjRolls += 1
                    if(j-1 >= 0):
                        if(arr2d[i+1][j-1] == "@"): adjRolls += 1
                if(adjRolls < 4): 
                    accessibleRolls += 1
                    toRemove.append([i, j])

        if not toRemove:
            print(accessibleRolls)
            exit(1)

        for i in range(len(toRemove)):
            index1 = toRemove[i][0]
            index2 = toRemove[i][1]
            arr2d[index1][index2] = "x"
        toRemove = []


zeroes = 0
position = 50

with open('day1/input.txt', 'r') as file:
    for line in file:
        currLine = line.strip()
        direction = currLine[0] #get first char
        turnAmt = int(currLine[1:]) #rest of string = num 
        if turnAmt > 100: #handle turns that revolve more than once
            numCycles = turnAmt // 100
            zeroes += numCycles
            for i in range(numCycles):
                turnAmt -= 100
        if direction == 'L' and position >= turnAmt: #turn left and doesnt go past 0
            if position == turnAmt: #turns to 0
                zeroes += 1
            position -= turnAmt
        elif direction == 'L' and position < turnAmt: #turn left and does go past 0
            if position != 0:
                zeroes += 1
            position = 100 - (turnAmt - position)
        elif direction == 'R' and position + turnAmt <= 100: #turn right and doesnt go past 0
            if position + turnAmt == 100: #turns to 0
                zeroes += 1
                position = 0
            else:
                position += turnAmt
        elif direction == 'R' and position + turnAmt > 100: #turn right and does go past 0
            position = (position + turnAmt) - 100
            zeroes += 1

print(zeroes)

    
    
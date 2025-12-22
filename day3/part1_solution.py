# 1 input line: 1 battery bank
# in 1 bank: turn on 2 batteries
# joltage : put together the digits (in order)
#goal: find largest joltage in each bank and sum

with open('day3/input.txt', 'r') as file:
    totalMaxJoltage = 0
    for line in file:
        currLine = line.strip()
        max1 = 0
        max2 = 0
        for i in range(0, len(currLine) - 1):
            if(int(currLine[i]) > max1): max1 = int(currLine[i])
        for i in range(currLine.index(str(max1)) + 1, len(currLine)):
            if(int(currLine[i]) > max2): max2 = int(currLine[i])
        maxJoltage = str(max1) + str(max2)
        print(maxJoltage)
        totalMaxJoltage += int(maxJoltage)

print(totalMaxJoltage)
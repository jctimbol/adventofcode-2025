# 1 input line: 1 battery bank
# in 1 bank: turn on 12 batteries
# joltage : put together the digits (in order)
# goal: find largest joltage in each bank and sum

with open('day3/input.txt', 'r') as file:
    totalMaxJoltage = 0
    
    for line in file:
        currLine = line.strip()
        digits = []

        for i in range(12): #every line
            if digits: 
                lowerBound = digits[-1] + 1
                if (digits[-1] + 1 < len(currLine)): currMaxIndex = digits[-1] + 1

            else: 
                lowerBound = 0
                currMaxIndex = 0

            upperBound = len(currLine) - 12 + i

            for j in range(lowerBound, upperBound + 1):
                if(int(currLine[j]) > int(currLine[currMaxIndex])): currMaxIndex = j
            digits.append(currMaxIndex)

        maxJoltage = ''
        for digit in digits:
            maxJoltage += currLine[digit]
        totalMaxJoltage += int(maxJoltage)

print(totalMaxJoltage)
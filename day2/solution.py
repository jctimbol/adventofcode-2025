# invalid : made only of some sequence of digits repeated twice
# odd amt of digits -> valid

totalInvalidIds = 0

with open('day2/input.txt', 'r') as file:
    idRanges = file.readline().split(",")
    for idRange in idRanges: #parse through all ranges
        invalidIds = 0
        bounds = idRange.split("-")
        lowBound = int(bounds[0])
        highBound = int(bounds [1])
        for i in range(lowBound, highBound): #parse through all ids in range
            idString = str(i)
            numDigits = len(idString)
            invalid = True
            if numDigits % 2 != 0:
                continue
            ptr1Idx = 0
            ptr2Idx = numDigits//2
            for j in range(0, numDigits//2): #parse through 1 id
                ptr1 = idString[ptr1Idx]
                ptr2 = idString[ptr2Idx]
                if(ptr1 != ptr2): invalid = False #not same sequence
                ptr1Idx += 1
                ptr2Idx += 1
            if invalid: invalidIds += i

        totalInvalidIds += invalidIds

print(totalInvalidIds)
totalInvalidIds = 0

def checkId(idString, numDigits):
    ptr1Idx = 0
    originalPtr2Idx = 1
    upperBound = 0
    #sloppy way to handle 3 digits  im tired
    if(numDigits==3): return (idString[0]==idString[1]==idString[2])
    if(numDigits%2 == 0): upperBound = numDigits // 2
    else: upperBound = numDigits // 2 - 1

    while(originalPtr2Idx <= upperBound):
        ptr1Idx = 0
        if(idString[ptr1Idx] == idString[originalPtr2Idx]):
            lastInSeq = idString[originalPtr2Idx-1]
            currPtr2Index = originalPtr2Idx
            while(idString[ptr1Idx] == idString[currPtr2Index]):
                if(currPtr2Index + 1 == numDigits):
                    if(idString[currPtr2Index] != lastInSeq): return False
                    return True
                ptr1Idx += 1
                currPtr2Index += 1
        originalPtr2Idx += 1
    return False

with open('day2/input.txt', 'r') as file:
    idRanges = file.readline().split(",")
    for idRange in idRanges:
        invalidIds = 0
        bounds = idRange.split("-")
        lowBound = int(bounds[0])
        highBound = int(bounds [1])
        for i in range(lowBound, highBound): #parse through all ids in range
            idString = str(i)
            numDigits = len(idString)
            if(numDigits<2): continue #all 1 digit ids are valid
            
            invalid = False

            invalid = checkId(idString, numDigits)

            if invalid: 
                print(idString, end = " ")
                print("invalid")
                invalidIds += i
        totalInvalidIds += invalidIds


print(totalInvalidIds)
        

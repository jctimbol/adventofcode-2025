ranges = []
ids = []
fresh = 0
with open('day5/input.txt', 'r') as file:
    readingRanges = True
    readingIds = False
    for line in file:
        if readingRanges:
            if not line.strip(): 
                readingRanges = False
                readingIds = True
                continue
            ranges.append(line.strip())

        if readingIds:
            ids.append(line.strip())

for id in ids:
    for oneRange in ranges:
        bounds = oneRange.split("-")
        lowBound = int(bounds[0])
        highBound = int(bounds[1]) + 1
        if int(id) in range(lowBound, highBound):
            fresh += 1
            break

print(fresh)
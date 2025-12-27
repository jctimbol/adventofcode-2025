ranges = []
fresh = 0
with open('day5/input.txt', 'r') as file:
    readingRanges = True
    for line in file:
        if readingRanges:
            currLine = line.strip()
            if not currLine: 
                readingRanges = False
                break
            bounds = currLine.split("-")
            lowBound = int(bounds[0])
            highBound = int(bounds[1])
            ranges.append([lowBound, highBound])

ranges.sort(key=lambda x:x[0])

mergedRanges = []
for oneRange in ranges:
    if not mergedRanges or oneRange[0] > mergedRanges[-1][1]:
        mergedRanges.append(oneRange)
    else: # overlap
        mergedRanges[-1] = [mergedRanges[-1][0], max(mergedRanges[-1][1], oneRange[1])]


fresh = 0
for oneRange in mergedRanges:
    fresh += (oneRange[1] - oneRange[0] + 1)

print(fresh)


import copy

freshranges = []
ingredients = []
with open("AoC-2025.txt") as file:
    for line in file:
        if "-" in line.rstrip():
            freshranges.append([int(x) for x in line.rstrip().split("-")])
        elif line.rstrip() == "":
            continue
        else:
            ingredients.append(int(line.rstrip()))

P1Solution = 0
for ing in ingredients:
    
    fresh = 0
    for frange in freshranges:
        if ing in range(frange[0], frange[1] + 1):
            fresh = 1

    if fresh == 1:
        P1Solution += 1

print("P1 Solution: " + str(P1Solution))

cleanranges = [freshranges[0]]
for frange in freshranges[1:]:

    mininrange = None
    maxinrange = None

    minindex = None
    maxindex = None

    rangesbetween = [x for x in cleanranges if (frange[0] < x[0] and frange[1] > x[1])]

    for betweenies in rangesbetween:
        cleanranges.remove(betweenies)

    for c, crange in enumerate(cleanranges):

        if frange[0] in range(crange[0], crange[1] + 1):
            mininrange = crange
            minindex = c
        if frange[1] in range(crange[0], crange[1] + 1):
            maxinrange = crange
            maxindex = c

    # [ ( ] ) [ ]
    if mininrange != None and maxinrange == None:
        cleanranges[minindex] = [mininrange[0], frange[1]]

    # [ ] ( [ ) ]
    elif mininrange == None and maxinrange != None:
        cleanranges[maxindex] = [frange[0], maxinrange[1]]

    # [ ( ] [ ) ]
    elif mininrange != None and maxinrange != None and mininrange != maxinrange:

        cleanranges.append([mininrange[0], maxinrange[1]])
        cleanranges.remove(mininrange)
        cleanranges.remove(maxinrange)
        sorted(cleanranges, key=lambda x: x[0])

    # [ ] ( ) [ ]
    elif mininrange == None and maxinrange == None:
        cleanranges.append([frange[0], frange[1]])
        sorted(cleanranges, key=lambda x: x[0])

    # No case needed for [ ( ) ]

P2Solution = 0
for crange in cleanranges:
    P2Solution += crange[1] - crange[0] + 1
print("P2 Solution: " + str(P2Solution))

    
    





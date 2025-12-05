import math

Data = []
with open("AoC-2025.txt") as file:
    for line in file:
        Data.append([int(x) for x in list(line.rstrip())])

P1Solution = 0
for line in Data:

    firstdigit = max(line[:-1])
    firstindex = line.index(firstdigit)

    maxj = 0
    for i in range(firstindex + 1, len(line)):

        test = int(str(firstdigit) + str(line[i]))
        if int(str(firstdigit) + str(line[i])) > maxj:
            maxj = int(str(firstdigit) + str(line[i]))

    P1Solution += maxj

print("P1 Solution: " + str(P1Solution))

P2Solution = 0
for line in Data:

    lbound = 0
    rbound = len(line) - 11

    maxdigit = []

    for i in range(0, 12):

        candidates = line[lbound:rbound]

        maxdigit.append(str(max(candidates)))
        lbound = candidates.index(max(candidates)) + lbound + 1
        rbound = len(line) - (11 - len(maxdigit))

    P2Solution += int("".join(maxdigit))
print("P2 Solution: " + str(P2Solution))













        






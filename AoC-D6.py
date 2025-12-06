import copy

numlines = []
strlines = []
with open("AoC-2025.txt") as file:

    for line in file:

        workingline = line.rstrip().split(" ")

        while '' in workingline:
            workingline.remove('')

        if workingline[0] == '*' or workingline[0] == '+':
            opline = workingline
        
        else:
            numlines.append([int(x) for x in workingline])
            strlines.append(list(line.rstrip()))

P1Solution = 0
for i, op in enumerate(opline):

    if op == "+":
        opsol = 0
        for numline in numlines:
            opsol += numline[i]

    elif op == "*":
        opsol = 1
        for numline in numlines:
            opsol *= numline[i]

    P1Solution += opsol

print("P1 Solution: " + str(P1Solution))

maxstrlen = max([len(x) for x in strlines])

for strline in strlines:
    while len(strline) < maxstrlen:
        strline.append(" ")

p2numlines = []
currnums = []
for i in range(maxstrlen - 1, -1, -1):

    newnum = ""

    for strline in strlines:
        newnum += strline[i]

    newnum = newnum.replace(" ", "")

    if newnum != "":
        currnums.append(int(newnum))

    else:
        p2numlines.append(currnums)
        currnums = []

    if i == 0:
        p2numlines.append(currnums)

P2Solution = 0
revops = opline[::-1]
for i, nums in enumerate(p2numlines):

    if revops[i] == "+":
        P2Solution += sum(nums)

    else:
        opsol = 1
        for num in nums:
            opsol *= num
        P2Solution += opsol

print("P2 Solution: " + str(P2Solution))

    

    

    

    









import math

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2025\AoC-2025.txt") as file:
    for line in file:
        Data = line.rstrip().split(",")

Ranges = []
for rangeinp in Data:
    Ranges.append([int(x) for x in rangeinp.split("-")])

def p1Sol(rangeinp):

    invalidids = []
    for i in range(rangeinp[0], rangeinp[1] + 1):

        if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:

            invalidids.append(i)

    return invalidids

P1Solution = 0
for rangeinp in Ranges:
    P1Solution += sum(p1Sol(rangeinp))
print("P1 Solution: " + str(P1Solution))

def p2Sol(rangeinp):

    invalidids = []
    for i in range(rangeinp[0], rangeinp[1] + 1):

        # We check the divisors for each int length - then we know which pieces we need to check
        divisors = [x for x in range(1, len(str(i)) + 1) if len(str(i)) % x == 0][:-1]

        for d in divisors:

            # Could shorten this part (remove dbit and dfull, no need for these variables), but the idea gets better across
            dbit = str(i)[:d]
            dfull = dbit * int((len(str(i)) / d))

            # Have to check if stuff is already in, else you enter 22222222 multiple times (with dbit 2, 22 and 2222)
            if dfull == str(i) and not(int(dfull) in invalidids):
                invalidids.append(i)

    return invalidids

P2Solution = 0
for rangeinp in Ranges:
    P2Solution += sum(p2Sol(rangeinp))
print("P2 Solution: " + str(P2Solution))




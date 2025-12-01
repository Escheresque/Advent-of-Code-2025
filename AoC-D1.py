import math

Data = []
with open(r"C:\Users\Roko\Desktop\RM Dateien\Projekte\AoC 2025\AoC-2025.txt") as file:
    for line in file:
        DataLine = []
        #for l in line.rstrip():
        #    DataLine.append(l)
        Data.append(line.rstrip())

# Really not the nicest solution, but at least systematic and the logic should be very clear :)

ordData = []
for inst in Data:
    ordData.append([inst[0], inst[1:]])

print("Test")

def p1Sol(currpos: int, instruction: str) -> int:

    if instruction[0] == "L":
        newpos = (currpos - int(instruction[1])) % 100

    else:
        newpos = (currpos + int(instruction[1])) % 100

    return newpos

def p2Sol(currpos: int, instruction: str, totalzeropass: int) -> int:

    shift = int(instruction[1])
    
    if instruction[0] == "L":

        newpos = (currpos - shift) % 100
        zeropass = 0

        if shift < 99:
            if currpos - shift <= 0 and currpos != 0:
                zeropass = 1

        else:
            if currpos == 0:
                zeropass += math.floor(shift/100)
            else:

                zeropass = 1
                reducedshift = shift - currpos
                zeropass += math.floor(reducedshift / 100)

    else:
        newpos = (currpos + shift) % 100
        zeropass = 0

        if shift < 99:
            if currpos + shift > 99 and currpos != 0:
                zeropass += 1

        else:
            if currpos == 0:
                zeropass += math.floor(shift/100)
            else:

                zeropass += 1
                reducedshift = shift - (100 - currpos)
                zeropass += math.floor(reducedshift / 100)
        
    return [newpos, totalzeropass + zeropass]

currpos = 50
counter = 0
for inst in ordData:
    newpos = p1Sol(currpos, inst)
    currpos = newpos
    if currpos == 0:
        counter += 1

print("P1 Solution: " + str(counter))

currpos = 50
counter = 0
zp = 0
for inst in ordData:
    step = p2Sol(currpos, inst, zp)
    currpos = step[0]
    zp = step[1]

print("P2 Solution: " + str(zp))



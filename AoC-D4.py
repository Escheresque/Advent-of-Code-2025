import copy

Data = []
with open("AoC-2025.txt") as file:
    for line in file:
        Data.append(list(line.rstrip()))

def accessornot(CurrData, i, j):

    around = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    paperrolls = 0

    if CurrData[i][j] == "@":

        for pos in around:

            checki = i + pos[0]
            checkj = j + pos[1]

            if (checki >= 0 and checki < len(CurrData)) and (checkj >= 0 and checkj < len(row)):

                if CurrData[checki][checkj] == "@":
                    paperrolls += 1

        if paperrolls < 4:
            return 1
        
        else: 
            return 0
        
    else: return 0
        
P1Solution = 0
for i, row in enumerate(Data):
    for j, col in enumerate(row):
        P1Solution += accessornot(Data, i, j)
print("P1 Solution: " + str(P1Solution))

continuewhile = 1
CurrData = copy.deepcopy(Data)
totalrolls = 0

while continuewhile == 1:

    startrolls = totalrolls

    continuewhile = 0
    for i, row in enumerate(CurrData):
        for j, col in enumerate(CurrData):

            rollaccess = accessornot(CurrData, i, j)
            
            if rollaccess == 1:

                totalrolls += 1
                CurrData[i][j] = "."
                continuewhile = 1

    if startrolls == totalrolls:
        continuewhile = 0

print("P2 Solution: " + str(totalrolls))



            





    

import copy

grid = []
with open("AoC-2025.txt") as file:
    for line in file:
        grid.append(list(line.rstrip()))

vizgrid = copy.deepcopy(grid)

newlaser = [grid[0].index("S")]
lasersplits = 0

for i, level in enumerate(grid[1:]):

    currlaser = copy.deepcopy(newlaser)
    newlaser = []

    for loc in currlaser:
        vizgrid[i][loc] = "|"

    for l, loc in enumerate(currlaser):

        if level[loc] == "^":
            
            lasersplits += 1
            
            if not loc - 1 in newlaser:
                newlaser.append(loc - 1)

            if not loc + 1 in newlaser:
                newlaser.append(loc + 1)

        elif not loc in newlaser:
            newlaser.append(loc)

print("P1 Solution: " + str(lasersplits))

vizgrid[0][grid[0].index("S")] = 1
for i, row in enumerate(vizgrid[0:]):
    for j, col in enumerate(row):

        if vizgrid[i][j] == "|":
            vizgrid[i][j] = 0

        if isinstance(vizgrid[i][j], int) and isinstance(vizgrid[i-1][j], int):
            vizgrid[i][j] += vizgrid[i-1][j]

        if isinstance(vizgrid[i][j], int) and (vizgrid[i][j-1] == "^" and isinstance(vizgrid[i-1][j-1], int)):
            vizgrid[i][j] += vizgrid[i-1][j-1]
        
        if isinstance(vizgrid[i][j], int) and j+1 < len(row):
            if vizgrid[i][j+1] == "^" and isinstance(vizgrid[i-1][j+1], int):
                vizgrid[i][j] += vizgrid[i-1][j+1]

P2Solution = 0
for sym in vizgrid[-2]:
    if isinstance(sym, int):
        P2Solution += sym

print("P2 Solution: " + str(P2Solution))



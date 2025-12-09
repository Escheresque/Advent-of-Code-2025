redtiles = []
with open("AoC-2025.txt") as file:
    for line in file:
        redtiles.append([int(x) for x in line.rstrip().split(",")][::-1])

def rectsize(p, q):
    return (abs(p[0] - q[0]) + 1) * (abs(p[1] - q[1]) + 1)

rects = []
for t, tile in enumerate(redtiles):
    for r, rile in enumerate(redtiles[t+1:]):
        rects.append([tile, rile, rectsize(tile, rile)])
rects.sort(key=lambda x: x[2])

redtilesset = set()

for tiles in redtiles:
    redtilesset.add((tiles[0], tiles[1]))

print("P1 Solution: " + str(rects[-1][2]))

# Bisschen erklärung für P2:
# Habe mit matplotlib mir die legaledge anzeigen lassen, wodurch ich bisschen info über die Form hatte
# dann habe ich die größte rectsize angeschaut und bemerkt, dass die Lösung max. 0.6 * (max(rectsize)) ist (eyeball)
# dann bin ich von da ausgehend hoch und es hat ca. 20min gedauert :) 
# Ein goldener stern ist ein goldener stern

legaledge = set()
for t, tile in enumerate(redtiles):
    legaledge.add((tile[0], tile[1]))

for t, tile in enumerate(redtiles): 

    print(str(t) + "/" + str(len(redtiles)))

    if t + 1 < len(redtiles):
        nexttile = redtiles[t + 1]

    else:
        nexttile = redtiles[0]

    if nexttile[1] != tile[1]:
        for g in range(min(nexttile[1], tile[1]) + 1, max(nexttile[1], tile[1])):
            legaledge.add((tile[0], g))

    if nexttile[0] != tile[0]:
        for g in range(min(nexttile[0], tile[0]) + 1, max(nexttile[0], tile[0])):
            legaledge.add((g, tile[1]))

def getinsideedge(p, q):

    smalledge = set()

    ul = (min(p[0], q[0]), min(p[1], q[1]))
    dl = (max(p[0], q[0]), min(p[1], q[1]))
    ur = (min(p[0], q[0]), max(p[1], q[1]))
    dr = (max(p[0], q[0]), max(p[1], q[1]))

    # Hallo Phillip wenn du weißt wie ich die coords der edges direkt als set eingeben kann und nicht den loop in der list comprehension machen muss, bitte sag mir Bescheid :(
    smalledge.update({(ul[0] + 1, r) for r in range(ul[1] + 1, ur[1])})
    smalledge.update({(d, ur[1] - 1) for d in range(ur[0] + 1, dr[0])})
    smalledge.update({(dl[0] - 1, l) for l in range(dl[1] + 1, dr[1])})
    smalledge.update({(u, ul[1] + 1) for u in range(ul[0] + 1, dl[0])})

    return smalledge

for r, rect in enumerate(rects[::-1]):

    if r % 10 == 0:
        print("Testing: " + str(r) + " of " + str(len(rects)) + " | rectsize: " + str(rectsize(rect[0], rect[1])))

    if rectsize(rect[0], rect[1]) > 1480000000 :
        continue

    insiderect = getinsideedge(rect[0], rect[1])
    overlaps = insiderect.intersection(legaledge)

    if len(overlaps) > 0:
        continue

    else:
        print("P2 Solution: " + str(rect[2]))
        break




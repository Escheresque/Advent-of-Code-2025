import math

# I am not proud of this

boxes = []
with open("AoC-2025.txt") as file:
    for line in file:
        boxes.append([int(x) for x in line.rstrip().split(",")])
boxes = sorted(boxes)

def eucdist(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)

connstocheck = []
for p, p1 in enumerate(boxes):
    for q1 in boxes[p+1:]:
        connstocheck.append([p1, q1, eucdist(p1, q1)])

connections = []
cables = 0
counter = 0
while counter < 1000:

    print(counter)

    onlydists = [x[2] for x in connstocheck]
    mindex = onlydists.index(min(onlydists))
    minpair = connstocheck[mindex]

    pin = None
    qin = None
    for c, conns in enumerate(connections):
        if minpair[0] in conns:
            pin = c
        if minpair[1] in conns:
            qin = c

    if pin == None and qin == None:
        connections.append([minpair[0], minpair[1]])
    elif pin != None and qin == None:
        connections[pin].append(minpair[1])
    elif pin == None and qin != None:
        connections[qin].append(minpair[0])
    elif (pin != None and qin != None) and pin != qin:
        fuse1 = connections[pin]
        fuse2 = connections[qin]
        connections.remove(fuse1)
        connections.remove(fuse2)
        fuse1.extend(fuse2)
        connections.append(fuse1)

    connstocheck.remove(minpair)
    counter += 1

connlengs = sorted([len(x) for x in connections], reverse=True)



connstocheck = []
for p, p1 in enumerate(boxes):
    for q1 in boxes[p+1:]:
        connstocheck.append([p1, q1, eucdist(p1, q1)])

connections = []
connectedboxes = []
cables = 0
counter = 0
while sorted(connectedboxes) != boxes:

    print("This takes a while..." + str(len(connectedboxes)) + " of " + str(len(boxes)))

    onlydists = [x[2] for x in connstocheck]
    mindex = onlydists.index(min(onlydists))
    minpair = connstocheck[mindex]

    pin = None
    qin = None
    for c, conns in enumerate(connections):
        if minpair[0] in conns:
            pin = c
        if minpair[1] in conns:
            qin = c

    if pin == None and qin == None:
        connections.append([minpair[0], minpair[1]])
        connectedboxes.append(minpair[0])
        connectedboxes.append(minpair[1])
    elif pin != None and qin == None:
        connections[pin].append(minpair[1])
        connectedboxes.append(minpair[1])
    elif pin == None and qin != None:
        connections[qin].append(minpair[0])
        connectedboxes.append(minpair[0])
    elif (pin != None and qin != None) and pin != qin:
        fuse1 = connections[pin]
        fuse2 = connections[qin]
        connections.remove(fuse1)
        connections.remove(fuse2)
        fuse1.extend(fuse2)
        connections.append(fuse1)

    connstocheck.remove(minpair)
    counter += 1



print("P1 Solution: " + str(math.prod(connlengs[0:3])))
print("P2 Solution: " + str(minpair[0][0] * minpair[1][0]))

    

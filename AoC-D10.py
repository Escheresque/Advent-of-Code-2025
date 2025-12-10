from itertools import product
from scipy.optimize import linprog

# Reading the input is the largest part of the code, i suck at this :)
machines = []
with open("AoC-2025.txt") as file:
    for line in file:

        workingline = line.rstrip().split(" ")
        machine = {}
        buttons = []

        for part in workingline:
            if part[0] == "[":
                light = []
                for sym in part[1:len(part) - 1]:
                    if sym == ".":
                        light.append(-1)
                    else:
                        light.append(1)
                machine["light"] = light

            if part[0] == "{":
                jolts = [int(x) for x in part[1:len(part) - 1].split(",")]
                machine["jolts"] = jolts

            if part[0] == "(":
                buttons.append([int(x) for x in part[1:len(part) - 1].split(",")])

        machine["buttons"] = buttons
        machines.append(machine)

for m, machine in enumerate(machines):

    bins = sorted(list(product([0, 1], repeat=len(machine["buttons"]))), key=sum)

    for presses in bins:

        currlight = [-1 for x in machine["light"]]

        for p, press in enumerate(presses):
            if press == 1:
                currbutton = machine["buttons"][p]
                for ind in currbutton:
                    currlight[ind] *= -1

        if currlight == machine["light"]:
            machine["llow"] = sum(presses)
            break

P1Solution = 0
for machine in machines:
    P1Solution += machine["llow"]
print("P1 Solution: " + str(P1Solution))

# P2 is just a min problem Ax = b with min(sum(x)) as a constraint

P2Solution = 0
for m, machine in enumerate(machines):

    obj = [1 for x in machine["buttons"]]
    inty = [1 for x in machine["buttons"]]
    A_eq = []

    for button in machine["buttons"]:
        buttonvect = [0 for x in machine["jolts"]]
        for pos in button:
            buttonvect[pos] = 1
        A_eq.append(buttonvect)

    A_eq = [list(i) for i in zip(*A_eq)]
    b_eq = machine["jolts"]

    opt = linprog(c=obj, A_eq=A_eq, b_eq=b_eq, method="highs", integrality=inty)
    P2Solution += sum(opt.x)

print("P2 Solution: " + str(P2Solution))

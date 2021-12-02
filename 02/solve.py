pos = {"f": 0, "d": 00, "u": 0, "a": 0}

def solve1():
    with open("input.txt", "r") as f:
        for ln in f:
            pos[ln[0]] += int(ln.split()[1])
    print(pos["f"] * (pos["d"] - pos["u"]))
    for key in pos:
        pos[key] = 0

solve1()

def solve2():
    with open("input.txt", "r") as f:
        for ln in f:
            k, j = ln.split()
            if k == "up":
                pos["a"] += int(j)
            elif k == "down":
                pos["a"] -= int(j)
            elif k[0] == "f":
                pos["f"] += int(j)
                pos["u"] += pos["a"] * int(j)
    print(pos["f"] * (pos["d"] - pos["u"]))

solve2()

# God forgive me, I did this in school, sorry

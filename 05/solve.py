import sys


def p1(npt) -> int:
    di = {}

    while True:
        try:
            s1, s2 = npt.readline().split(" -> ")
            x1, y1 = map(int, s1.split(","))
            x2, y2 = map(int, s2.split(","))
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1
        except Exception:
            break

    return len([each for each in di if di[each] > 1])


def p2(npt) -> int:
    di = {}

    while True:
        try:
            s1, s2 = npt.readline().split(" -> ")
            x1, y1 = map(int, s1.split(","))
            x2, y2 = map(int, s2.split(","))
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1
            elif abs(x1 - x2) == abs(y1 - y2):
                dx = -1 if x1 > x2 else 1
                dy = -1 if y1 > y2 else 1
                x, y = x1, y1
                while True:
                    di[(x, y)] = 1 if (x, y) not in di else di[(x, y)] + 1
                    if (x, y) == (x2, y2):
                        break
                    x += dx
                    y += dy
        except Exception:
            break

    return len([each for each in di if di[each] > 1])


def main() -> int:
    """Entry/main function"""

    a = open("input.txt", "r")
    print(p1(a))
    a.close()
    a = open("input.txt", "r")
    print(p2(a))
    a.close()

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"
    sys.exit(main())

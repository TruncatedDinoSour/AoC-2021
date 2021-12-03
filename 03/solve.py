import sys


def bit_criteria(input, bit=0, opposite=False):
    counter_0 = 0
    counter_1 = 0
    for binnum in input:
        if binnum[bit] == "0":
            counter_0 += 1
        else:
            counter_1 += 1

    if not opposite:
        return "0" if counter_0 > counter_1 else "1"

    return "1" if counter_0 > counter_1 else "0"


def filter_by(input, criteria, bit=0):
    filtered = set()
    for binnum in input:
        if binnum[bit] == criteria:
            filtered.add(binnum)

    return filtered


def main() -> int:
    """Entry/main function"""

    with open("input.txt", "r", encoding="utf-8") as f:
        npt = f.readlines()

        bits = [0] * len(npt[0].strip())

        e = ""
        g = ""

        for line in npt:
            line = line.strip()

            for idx, letter in enumerate(line):
                bits[idx] += int(letter)

        for bit in bits:
            g += str(int(bit > len(npt) / 2))
            e += str(int(bit < len(npt) / 2))

        print(int(e, 2) * int(g, 2))  # D3P1

        OX = set(npt)
        CO2 = set(npt)

        bit = 0
        while len(OX) > 1:
            OX_criteria = bit_criteria(OX, bit)
            OX = filter_by(OX, OX_criteria, bit)
            bit += 1

        bit = 0
        while len(CO2) > 1:
            CO2_criteria = bit_criteria(CO2, bit, opposite=True)
            CO2 = filter_by(CO2, CO2_criteria, bit)
            bit += 1

        print(int(OX.pop(), 2) * int(CO2.pop(), 2))  # D3P2

        return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"
    sys.exit(main())

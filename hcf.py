def list_hcf(l):
    hcf = l.pop(0)
    for i in l:
        hcf = hcf2(hcf, i)
    return hcf


def hcf2(a, b):
    r = a % b
    while r > 0:
        a, b = b, r
        r = a % b
    return b


if __name__ == "__main__":
    n = int(input("How many numbers you want to get hcf of: "))
    l = []
    for i in range(1, n + 1):
        l.append(int(input(f"{i}:")))
    print("The hcf of the following numbers is", list_hcf(l))

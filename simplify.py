from hcf import list_hcf


def simplify(frac):
    if frac[1] == 0:
        raise ValueError("Denominator cannot be zero")
    elif frac[0] == 0:
        return [0, 1]

    hcf = list_hcf(frac)
    sfrac = [int(frac[0]/hcf), int(frac[1]/hcf)]
    return sfrac


def main():
    f = input("Enter a fraction:")
    f = f.split(sep='/')
    f[0] = int(f[0])
    f[1] = int(f[1])
    sf = simplify(f)
    print(f"Its simplified form is {sf[0]}/{sf[1]}")


if __name__ == "__main__":
    main()

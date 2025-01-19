def dec2bin(x, numdec = 10):
    out = "."
    intx = int(x)
    decx = x - intx
    conv_int = (intx <= 0)
    if conv_int:
        out = "0" + out
    while not conv_int:
        out = str(intx % 2) + out
        intx -= intx % 2
        intx //= 2
        conv_int = (intx == 0)
    pow2 = 0.5
    for _ in range(numdec):
        if decx >= pow2:
            out = out + str("1")
            decx -= pow2
        else:
            out = out + str("0")
        pow2 /= 2
    return out

## DEMO ##
num_to_test = [5, 10, 0.5, 0.25, 0.2, 0.1, 0.3]

for _n in num_to_test:
    print(str(_n) + " in binario diventa " + dec2bin(_n, 50))


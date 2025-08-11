def GRC(a,b):
    while b != 0:
        a,b = b, a%b
    return a

grc = GRC(12,18)
print(grc)
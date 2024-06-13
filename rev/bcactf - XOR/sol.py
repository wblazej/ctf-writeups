x = "21 0F 0A 15 3F 29 29 6B 13 1C 2C 74 7D 30 5E 50 6E 29 2B 24 19 0C 67 7D 05 54 7C 34 5C 13 32 42 29 62 7B 0F 4E"

a = "ClkvKOR8JQA1JB731LeGkU7J4d2khDvrOPI63mM7"
x = [int(i, 16) for i in x.split()]

print(''.join([chr(aa ^ xx) for aa, xx in zip(bytes(a.encode()), x)]))
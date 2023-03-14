def f1(x, y, z):
    s = x + y + z
    return s / 3.0

def f2(x, y, z=0, p=1):
    return f1(x, y, z)

print(f2(2, 3, 4))

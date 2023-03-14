def make_incrementor(n):
    return lambda x: x + n

a = make_incrementor(3)
print(a(10))
print(a(20))
print(a(30))

print((lambda x,y,z: x + y + z)(1,2,3))
def f(x, y, z): return x + y + z
print(f(1,2,3))
def f23(x):
    pass
    return x * 2

def f0(x):
    print("called f0")

a = f0(123)
print(a)

x = 1
z = f23(x)
print(z)

a = 4
z = f23(a)
print(z)

z = f23("abc")
print(z)

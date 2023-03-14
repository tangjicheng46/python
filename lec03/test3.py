def func(x):
    if x <= 1:
        return 1
    return func(x - 1) + func(x - 2)

def func2(x):
    if x <= 1:
        return 1
    a = 0
    b = 1
    i = 0
    while i < x:
        tmp = a + b
        a = b 
        b = tmp 
        i = i + 1
    return b
# a b a+b
#   a  b  
# print(func(100))
print(func2(100))
def f0(x):
    def func(): return x + 1
    return func 

print(f0(1)())

def func(x): return x + 1
lambda x: x+1
# 上面两种函数定义方式，完全等价

def f1(x):
    return lambda : x+1
print(f1(1)())
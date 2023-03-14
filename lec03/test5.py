def f0(x):
    print("call f0")
    x()

def f1():
    print("call f1")
    # return 1111
    # return None
    # 没有写return，那么就是return None
    return 1111

# f0(f1)

print(f1)
print(f1())
# 函数f，也是一个东西。（对象）
# 一切皆对象

# 不加括号，不调用f，f本身是一个对象
# 如果后面跟着括号，表示f的调用

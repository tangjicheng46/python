# 函数

```
def fn(x1, x2, xk, ..., xn):
    pass 

xk 如果有默认值，
xk+1 ... xn必须有默认值
```

python函数，不仅可以递归调用，还可以递归定义。  
```
def f0():
    def f1():
        print("haha")
    f1()

f0()
```

递归调用的例子，费布那切数列的例子  
```
def func(x):
    if x <= 1:
        return 1
    return func(x - 1) + func(x - 2)
```

lambda表达式  
```
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
```

# 元组
与列表类似，但是元组的元素是不可变的。

list(元组)： 元组->列表
tuple(列表): 列表->元组

# 字典
一种映射关系，练习在test9.py

# python最常用的三种复合结构
列表，元组，字典
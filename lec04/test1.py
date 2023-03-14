class A:
    def __init__(self, number):
        self.color = number 
        print("hahahahaha")
        self.size = 123
    
    def print2(self):
        self.abc = 111
        print(self.color)

x = A(1)
print(x.color)
x.abc = 1
print(x.abc)
x.print2()
print(x.abc)

# a = A(10)
# print(a.color)
# print(a.size)
# a.size = 12
# a.print2()

# b = A(13)
# print(b.color)
# print(b.size)
# b.size = 44
# b.print2()

# a.print2()

# 描述数据，描述行为

# 凡是用两个下划线开头，并且两个下划线结尾的，方法。都称之为，魔法方法。magic。
# 这些方法，是python语言自己保留的方法，有相应的特殊用途。
# 我们自己命名的方法，请不要使用两个下划线开头。
def f1():
    print("f1")
    
class Func:
    def __call__(self):
        print("f2")

x = Func()
x()
f1()

# function is a kind of callable object.
# f()
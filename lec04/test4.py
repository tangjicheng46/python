class Human:
    def __init__(self, h, w):
        self.h = h 
        self.w = w 

    def run(self):
        print("height", self.h)
        print("weight", self.w)

class Student(Human):          # 1
    def __init__(self, h, w, code):
        super().__init__(h, w) # 2
        self.code = code 

    def run(self):
        super().run()          # 3
        print("code", self.code)


a = Student(166, 66, 99999)
a.run()

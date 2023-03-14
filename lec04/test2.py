class Student:
    CLASS_NAME = "3grade_2class"

    def __init__(self, height, weight):
        print("正在生成学生...")
        self.height = height 
        self.weight = weight

    def run(self):
        print("正在跑步中...")
        print("self.height", self.height)
        print("self.weight", self.weight)
        print("my class name: ", Student.CLASS_NAME)
    
    @classmethod
    def Clean(cls):
        print("教室正在被打扫...")

xiao_ming = Student(166, 66)
print("hahahahaha")
xiao_ming.run()

Student.Clean()

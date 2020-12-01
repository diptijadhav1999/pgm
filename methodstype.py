class student:

    school="svpm"

    def __init__(self,m1,m2,m3):
        self.m1=m1                  #self is a instance method
        self.m2=m2
        self.m3=m3

    def average(self):
        print((self.m1+self.m2+self.m3)/3)

    @classmethod                #decorator for class method
    def getschool(cls):
        print("This is a class method")

    @staticmethod               #decorator for static method
    def info():
        print("This is static method")


s1=student(2,3,4)
s2=student(3,4,5)
s1.average()
student.getschool()
s1.info()    #decorator uses

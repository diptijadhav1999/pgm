#inheritance in object oriented programming

class A:
    def student1(self):
        print("this is student1")

    def student2(self):
        print("this is student2")

class B(A):    #single level inheritance
    def student3(self):
        print("this is student3")

    def student4(self):
        print("this is student4")


'''class C(A,B):             #multiple inheritance
    def student5(self):
        print("this is student5")

    def student6(self):
        print("this is student6")
'''

a1=A()
b1=B()
#c1=C()
b1.student3()
#class inside another class
class school:

    def __init__(self,name,id1):
        self.name=name
        self.id1=id1
        self.lap=self.branch("yahoo",4)

    def show(self):
        print(self.name,self.id1)

    class branch:
        def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno

        def show(self):
            print(self.name,self.rollno)

s1=school("svpm",1)
s1.show()

#s2=school.branch("computer",426)         #first method
#s2.show()

print(s1.lap.name)                        #second method
print(s1.lap.rollno)
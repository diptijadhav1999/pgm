class computer:

    def __init__(self):
        self.name="dipti"
        self.age=22

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.age=10
if c1.compare(c2):
    print("they re same")
else:
    print("they are different")

print(c1.name)
print(c1.age)
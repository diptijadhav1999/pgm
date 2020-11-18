class computer:

    def __init__(self,cpu,ram):
        print("in init")
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("congig is ",self.cpu,self.ram)




comp1=computer("i3",4)
comp1.config()
computer.config(comp1)   # second method

a=5
a.bit_length()
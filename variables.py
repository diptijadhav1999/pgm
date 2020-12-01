class variables:

    from_it_is="gadgets"                #class variables/static variables

    def __init__(self,processor,ram):
        self.processor=processor        #instance variables
        self.ram=ram

    def display(self):
        print("display",self.processor,self.ram)




l1=variables("i5",8)
l2=variables("i3",4)

l1.display()
l2.display()
print(l1.from_it_is)

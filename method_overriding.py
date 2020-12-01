class x:
    def show(self):
        print("in x")

class y(x):
    #def show(self):
     #   print("in Y")
    pass
x1=y()
x1.show()
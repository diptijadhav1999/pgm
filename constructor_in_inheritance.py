class one:

    def __init__(self):
        print("this is one init")

    def show(self):
        print("show in one class")

class two:

    def __init__(self):

        print("this is two init")


    def show1(self):
        print("show in two class")

class three(two,one):
    def show2(self):
        super().show()
        print("show in three class")

#o1=one()
#o1.show()
t1=three()
t1.show2()
class school:

    def code(self,ide):
        ide.execute()

class pycharm:

    def execute(self):
        print("compiling")

class myeditor:

    def execute(self):
        print("running")

#ide=pycharm()
s1=school()
s1.code(pycharm())
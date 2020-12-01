from threading import *
from time import sleep

class helloji(Thread):

    def run(self):
        for i in range(5):
            sleep(1)
            print("hello")

class hiji(Thread):

    def run(self):
        for i in range(5):
            sleep(1)
            print("hi")

a1=helloji()
a2=hiji()

a1.start()
sleep(0.2)
a2.start()

a1.join()
a2.join()
print("stop")
from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def show(self):
        pass

class laptop(computer):

    def show(self):
        print("hello")

c1=laptop()
c1.show()
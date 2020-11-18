import sys

print(sys.setrecursionlimit(2000))
print(sys.getrecursionlimit())
def greet():
    print("hello")
    greet()
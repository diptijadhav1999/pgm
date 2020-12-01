a=10
b=2
try:
    print("file open")
    print(a/b)
    x=int(input("enter the number"))
    print(x)
except ZeroDivisionError as e:
    print("zero division error",e)

except ValueError as e:
    print("invalid input")

except Exception:
    print("something went wrong")

finally:
    print("file close")
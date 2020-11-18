a=10
print(id(a))
def some():

    a=9
    x=globals()['a']
    print(id(x))

    print("infunction",a)
    globals()['a']=15    #changing the value of global variable without affecting the local variables
    print(id(a))
some()
print("outfunction",a)

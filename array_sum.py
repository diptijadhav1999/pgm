
def sumelement(y):
    sum=0
    for value in y:
        sum=sum+value
    return sum

n=int(input("enter testcase"))
for x in range(n):
    y=list(map(int,input("enter the array element").split()))
    print(sumelement(y))

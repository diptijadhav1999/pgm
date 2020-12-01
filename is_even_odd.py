def isoddevendifference(x):
    even=0
    odd=0
    for i in x:
        if i%2==0:
            even=even+i
        else:
            odd+=i
    return even-odd


n=int(input())

x=list(map(int,input().split()))
print(isoddevendifference(x))

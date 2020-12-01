def sumdigit(arr):

    lst=[]

    for x in arr:
        sum=0
        while(x!=0):
            rem=x%10
            sum=sum+rem
            x=x//10
        lst.append(sum)
    return lst

t=int(input("testcases"))
for i in range(t):
    x=list(map(int,input("enter arr").split()))
    print(sumdigit(x))

from array import *
arr=array("i",[])
n=int(input("enter the length of the array"))
for i in range(n):
    x=int(input())
    arr.append(x)
print(arr)
val=int(input())
k=0
for e in arr:
    if e==val:
        print(k)
    k=k+1
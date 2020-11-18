
from functools import reduce    #for reduce

nums=[2,3,1,4,21,6]
even=list(filter(lambda x:x%2==0,nums))
print(even)

double=list(map(lambda x:x*2,even))
print(double)

redu=reduce(lambda x,y:x+y,nums)
print(redu)
class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        sum1=self.m1+other.m1
        sum2=self.m2+other.m2
        s3=student(sum1,sum2)
        return s3

#x,y=map(int,input().split(","))
s1=student(1,2)
s2=student(11,12)
s3=s1+s2
print(s3.m1,s3.m2)
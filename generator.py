def topten():

    n=1
    while n<=10:
        square=n*n
        yield square
        n+=1

values=topten()
for i in values:
    print(i)
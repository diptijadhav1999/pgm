
i=0
j=0
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")

        i=i+1
        #j=j+1
    print()
for i in range(0,5):
    for j in range(1,5-i):
        print("*",end=" ")
        i=i-1
    print()
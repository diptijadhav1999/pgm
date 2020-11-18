def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
            
        else:
            odd=odd+1
    return even,odd

lst=[20,25,14,13,24,28,43]
even,odd=count(lst)
print("even:{} and odd:{}".format(even,odd))
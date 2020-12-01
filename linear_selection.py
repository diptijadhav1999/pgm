pos=-1
def search(nums,n):
    #i=0
    #while i< len(nums):
    for i in range(len(nums)):
        if nums[i]==n:
            globals()["pos"]=i
            return True
        #i=i+1
    return False


nums=[6,5,2,1,8,9]
n=1
if search(nums,n):
    print("found at",pos)
else:
    print("not found")
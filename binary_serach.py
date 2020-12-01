pos=-1
def search(nums,n):
    l=0
    u=len(nums)-1
    while l<=u:

        mid=(l+u)//2
        if nums[mid]==n:
            globals()["pos"]=mid
            return True
        else:
            if nums[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
nums=[1,3,5,7,9,10,44,56,78,90]
n=3
if search(nums,n):
    print("found",pos+1)
else:
    print("not found")
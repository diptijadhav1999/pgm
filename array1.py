from numpy import *
arr=array([22,4,66,0])
arr1=arr.view()      #view is use to create array at different memory location
print(id(arr),id(arr1))
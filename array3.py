from numpy import *
array1=array([[1,2,3],[4,5,6]])
print(array1)


print(array1.dtype)
print(array1.ndim)
print(array1.shape)
print(array1.size)
arr=array1.flatten()
print(arr)
arr1=array1.reshape(1,3,2)
print(arr1)

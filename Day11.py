import numpy as np
a = [[1,2,3],[4,5,6]]
b = np.array(a)
print(b)

print(b.ndim)
print(b.shape)
print(b[0,0])
print(b[0,1])

#print(np.zeros((2,2)))

c = np.zeros((2,2))
print(c)
print(" ")
print(np.ones((3,3)))

print(np.full((3,3),2))

print()
print(np.eye(3))

a = np.arange(20)
print()
print(a)

b=a.reshape((5,4))
print()
print(b)

import numpy as np
st = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
arr = np.array(st)
a = arr[0:2, 0:2]
print(a)
print()
print()
print()

a= arr[1:2, 1:2]
print(a)
print()
print()
print()

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

c=a+b
print(c)
print()
print()
print()

c= a/b
print(c)
print()
print()
print()

c = np.add(a,b)
print(c)
print()
print()
print()

import numpy as np
arr1 = [[1,2],[3,4]]
arr2 = [[5,6],[7,8]]
a = np.array(arr1)
b = np.array(arr2)

c = np.dot(a,b)
print(c)
print()
print()
print()

import numpy as np
a = np.array([[-1,2,3],[3,4,8]])
s = np.sum(a)
print("sum= ",a.sum())

print()
print()
print()

print('sum by row=',a.sum(axis=0))

print()
print()
print()

print('mean=',a.mean())

print()
print()
print()

print('sd=',a.std())

print('product=',a.prod())
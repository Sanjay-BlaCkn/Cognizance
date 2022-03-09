lst1 = []
n = int(input("ENTER NUMBER OF ELEMENTS TO BE ADDED TO ARRAY : "))
print("ENTER THE ELEMENTS TO BE ADDED : ")
for i in range(0, n):
    b = int(input())
    lst1.append(b)
print(lst1)
lst2 = []
m = int(input("ENTER NUMBER OF ELEMENTS TO BE ADDED TO ARRAY : "))
print("ENTER THE ELEMENTS TO BE ADDED : ")
for i in range(0, m):
    a = int(input())
    lst2.append(a)
print(lst2)

import numpy as np
x = np.array(lst1)
print("First array:")
print(x)
y = np.array(lst2)
print("Second array:")
print(y)
print("Are above two arrays are equal! : ")
array_equal = np.allclose(x, y)
print(array_equal)
lst = []
n = int(input("ENTER NUMBER OF ELEMENTS TO BE ADDED TO ARRAY : "))
print("ENTER THE ELEMENTS TO BE ADDED : ")
for i in range(0, n):
    b = int(input())
    lst.append(b)
print(lst)

import numpy as np
lst= np.array(lst)
print("Original array:")
print(lst)
p = 5
new_lst = np.zeros(len(lst) + (len(lst)-1)*(p))
new_lst[::p+1] = lst
print("\nNew array:")
print(new_lst)

import numpy as np
print("EXERCISE TO ADD TWO ARRAYS")
lst1 = []
n = int(input("ENTER NUMBER OF ELEMENTS TO BE ADDED TO ARRAY-1 : "))
print("ENTER THE ELEMENTS TO BE ADDED : ")
for i in range(0, n):
    b = int(input())
    lst1.append(b)
print(lst1)
lst2 = []
m = int(input("ENTER NUMBER OF ELEMENTS TO BE ADDED TO ARRAY-2 : "))
print("ENTER THE ELEMENTS TO BE ADDED : ")
for i in range(0, m):
    a = int(input())
    lst2.append(a)
print(lst2)
array1 = np.array(lst1)
array2 = np.array(lst2)
   
print ("1st Input array : ", array1) 
print ("2nd Input array : ", array2) 
    
out_arr = np.add(array1, array2) 
print ("ANSWER AFTER ADDING TWO ARRAY : ", out_arr) 
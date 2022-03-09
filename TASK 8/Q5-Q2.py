print("ENTER THE VALUES FOR FIRST MATRIX")
R = int(input("Enter the number of rows needed :"))
C = int(input("Enter the number of columns needed :"))
matrix1 = []
print("Enter the entries row wise :")
for i in range(R): 
    a =[]
    for j in range(C):
         a.append(int(input()))
    matrix1.append(a)
for i in range(R):
    for j in range(C):
        print(matrix1[i][j], end = " ")
    print()
print("")


print("ENTER THE VALUES FOR SECOND MATRIX")
R = int(input("Enter the number of rows needed :"))
C = int(input("Enter the number of columns needed :"))
matrix2 = []
print("Enter the entries rowwise:")
for i in range(R): 
    a =[]
    for j in range(C):
         a.append(int(input()))
    matrix2.append(a)
for i in range(R):
    for j in range(C):
        print(matrix2[i][j], end = " ")
    print()
print("")


print("ANSWER AFTER MULTIPLYING THE ABOVE TWO MATRIX")
X = (matrix1)
Y = (matrix2)
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
for r in result:
   print(r)
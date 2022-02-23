r = 5
s = r - 1
for i in range(0, r):
     for j in range(0, s):
            print(end=" ")
     s = s - 1
     for j in range(0, i+1):
         print("* ", end="")
     print("\r")

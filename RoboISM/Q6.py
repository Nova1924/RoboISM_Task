l = int(input("Lower Limit of the range"))
u = int(input("Upper Limit of the range"))


for i in range(l, u + 1):
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(str(i) + " " , end = "")
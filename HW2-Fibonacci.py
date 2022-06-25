
n=int(input("Enter number of fibo series: "))
FL=[]
for i in range(n):

    if i<2:
        FL.append(1)
    else:
       f= FL[i-1]+ FL[i-2]
       FL.append(f)
       
print("FL=",FL)


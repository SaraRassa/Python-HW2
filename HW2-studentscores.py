scores=[]
n=int(input("Enter number of students: "))
sum=0
for i in range(n):
    x=float(input("Student score: "))
    sum=sum+x
    scores.append(x)

average=sum/n
MAX=max(scores)
MIN=min(scores)
scores.sort()
print("student scores from low to high: ",scores)
print("Average= ",average ,"\nMaximum score= ",MAX,"\nMinimum score= ",MIN)

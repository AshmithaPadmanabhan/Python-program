a=list(map(int,input("Enter the array:").split()))
n=len(a)
l=[]
sum1=sum(a)
total=0
for i in range(n):
    sum1-=a[i]
    total+=a[i]
    sum2=total-a[i]
    d=abs(sum1-sum2)
    l.append(d)
print(l)
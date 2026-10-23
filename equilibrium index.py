a=list(map(int,input("Enter the array:").split()))
n=len(a)
sum1=sum(a)
total=0
count=0
for i in range(n):
    sum1-=a[i]
    total+=a[i]
    sum2=total-a[i]
    if sum1==sum2:
        count+=1
if count==0:
    print(-1)
else:
    print(count)
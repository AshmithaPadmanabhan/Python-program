a=list(map(int,input("Enter the array:").split()))
n=len(a)
count=0
total=sum(a)
for i in range(n):
    prefix=total
    total-=a[i]
    if prefix%2==0:
        count+=1
print(count)
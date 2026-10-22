n=int(input("No of elements:"))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
count=0
total=sum(a)
prefix_sum=0
for i in range(n-1):
    prefix_sum+=a[i]
    sufix_sum=total-prefix_sum
    d=sufix_sum-prefix_sum
    if d%2==0:
        count+=1
print(count)
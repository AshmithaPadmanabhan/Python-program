n=int(input("Enter the no of elements:"))
a=[]
count=0
for i in range(n):
    x=int(input())
    a.append(x)
for i in range(n-2):
    if a[i+1]==a[i]+a[i+2]:
        count+=1
print(count)

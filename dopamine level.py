n=int(input("Enter the no of elements:"))
l=int(input("Enter low range:"))
r=int(input("Enter high range:"))
a=[]
l1=[]
d=0
for i in range(n):
    x=int(input())
    a.append(x)
for i in a:
    if i>=l and i<=r:
        d+=1
        l1.append(d)
    else:
        d-=1
        l1.append(d)
print(max(l1))
print(min(l1))

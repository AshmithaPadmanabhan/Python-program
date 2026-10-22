n=int(input("Enter the no of elements:"))
a=[]
l=[]
for i in range(6):
    x=int(input())
    a.append(x)
for i in range(n):
    if i==0 or i==1:
        l.append(a[i])
    else:
        l.append(l[i-2]+l[i-1])
for i in l:
    print(i,end=' ')

n=int(input("Enter the no of elements:"))
a=[]
l=[]
for i in range(n):
    x=int(input())
    a.append(x)
for i in range(n):
    c=0
    if a[i]<a[i-1]:
        c+=1
    if i!=n-1:
        if a[i]<a[i+1]:
            c+=1
    else:
        if a[i]<a[0]:
            c+=1
    print(c)
    l.append(c)
print(l)
    

n=int(input("No of elements:"))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
prefix=[]
sufix=[]
position,count=0,0
def sp(position,count):
    st,pt=0,0
    for i in range(position+1):
        pt+=a[i]
        prefix.append(pt)
    print(prefix)
    for j in range(n-1,position,-1):
        st+=a[j]
        sufix.append(st)
    print(sufix)
    if prefix==[] or sufix==[]:
        return count
    else:
        d=prefix[-1]-sufix[-1]
        if d%2==0:
            count=count+1
        position+=1
        if position<=n-1:
            prefix.clear()
            sufix.clear()
            return sp(position,count)
c=sp(position,count)
print(c)


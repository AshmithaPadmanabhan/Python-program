a=list(map(int,input("Enter the elemts:").split()))
count=0
n=len(a)
for i in range(len(a)-2):
    if a[i+1]==a[i]+a[i+2]:
        count+=1
print(count)

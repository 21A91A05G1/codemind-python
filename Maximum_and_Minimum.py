n=int(input())
arr=list(map(int,input().split()))
b=[]
d=[]
c=0
for i in arr:
    if i==arr.count(i):
        c+=1
        b.append(i)
if(c==0) :
    print("-1")
else:
    print(min(b),max(b),end=" ")
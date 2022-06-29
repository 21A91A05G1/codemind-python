n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=set(a)
k=set(b)
c=0
c1=0

for i in d:
    if i not in k:
        c1+=1
for i in k:
    if i not in d:
        c+=1
print(c+c1)    
n=int(input())
arr=list(map(str,input().split()))
b=[]
c=0
for i in arr:
    b.append(len(i))
m=max(b)    
for i in arr:
    if(len(i)==m):
        print(i,end=" ")
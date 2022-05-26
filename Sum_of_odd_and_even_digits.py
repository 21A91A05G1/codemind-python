n=int(input())
s=0
s1=0
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if i%2!=0:
        s=s+arr[i]
    else:
        s1=s1+arr[i]
res=(s1-s) 
if(res==0):
    print("YES")
else:
    print("NO")
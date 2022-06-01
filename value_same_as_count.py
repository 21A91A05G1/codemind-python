n=int(input())
b=[]
arr=list(map(int,input().split()))
for i in arr:
    if(i==arr.count(i)):
        b.append(i)
b=set(b)
print(len(b))

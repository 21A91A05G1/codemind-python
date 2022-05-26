n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if arr[j]<arr[i]:
            c+=1
    print(c,end=' ')        
    
def isprime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        return 1
n=int(input()) 
arr=list(map(int,input().split()))

sum=0
c=0
for i in arr:
    if(isprime(i)==1):
    
        c+=1
print(c)
        
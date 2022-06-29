def isprime(n):
    if(n==1):
        return -1
    for i in range(2,n):
        if(n%i==0):
            return -1
    else:
        return 1
n=int(input()) 
arr=list(map(int,input().split()))
a=int(input())
d=[]
sum=0
c=0
for i in arr:
    if(isprime(i)==1):
        d.append(i)
for i in d:
    if(i>=a):
        c+=1
print(c)
        
n=int(input())
pr=1
flag=0
for i in range(1,n+1):
    pr=i*i
    if(n==pr):
        flag=1
if(flag==1):
    print("True")
else:
    print("False")
    

n=int(input())
n1=n
for i in range(1,n,1):
    if(n%i==0):
        temp=i*(i+1)
        if(n1==temp):
            print("YES")
            break
else:
    print("NO")
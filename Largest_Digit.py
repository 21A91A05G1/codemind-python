n=int(input())
temp=n
large=0
while(n):
    d=n%10
    n=n//10
    if(d>large):
        large=d
        
print(large)
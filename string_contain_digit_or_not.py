s=input()
s=s.lower()
c=0
k="0123456789"
for i in s:
    if i in k:
        c+=1
if(c==0):        
    print("Doesn't contain digit")
    
else:
    print("Contains %d digit"%c)
        
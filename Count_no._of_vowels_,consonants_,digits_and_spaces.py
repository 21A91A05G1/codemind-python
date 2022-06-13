s=input()

v=0
c=0
d=0
k=0
for  i in s:
    if i in 'aeiou':
        v+=1
    if i not in"aeiou" and i not in "0123456789" and i not in " ":
        c+=1
        
    if i in '0123456789':
        d+=1
    if i in " ":
        k+=1
    
print("Vowels:",v) 
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",k )

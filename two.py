a=input()
print(a.count('b'))
c=0
b=len(a)
z=[]
while b>0:
    d=(a[c],a.count(a[c]))
    if d not in z:
        z.append(d)
    b-=1
    c+=1
print(z)



a=set(input())
b=set(input())
d=[]
def sort():
    c.sort()
    b=''
    for i in c:
        b+=i
    c.clear()
    d.append(b)

c=[]
c.extend(a.intersection(b))
sort()
c.extend(a-b)
sort()
c.extend(b-a)
sort()
print(d)


def shift(a):
    list=a
    number=int(input())
    if number>0:
        c=0-number
        b=list[:c]        
        a=[]
        d=-1
        while number>0:
            a.append(list[d])
            number-=1
            d-=1    
        a.extend(b)  
        print(a)
    elif number<0:
        c=list[number-1:]
        d=list[:number-1]
        c.extend(d)
        print(c)

shift([1,2,3,4,5])


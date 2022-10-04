def rotateArray(a, d):           
    n = len(a)
    if d > 0:                                          
        a[:] = a[-d:n] + a[:-d] 
                                                    
        if d > n:                                       
            d = d % n                                   
            print(a)
       
    else:
        a[:] = a[-d:n] + a[:-d]

    return a
list = list(map(int,input('Enter a list?').strip().split()))
number = int(input('Enter a number?'))

print(rotateArray(list,number))


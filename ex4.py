def nearestFun(i):
 while i>0:
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                if y:
                    return i
        i = i-1             



Num = list(map(int, input("please enter numbers seperated by space, press enter to finish Entering: ").split()))
multi=1
for i in Num:
    multi = i*multi
print(nearestFun(multi))
num1=int(input())
num2=int(input())
num3=int(input())

for i in range(1,num1*num2*num3):    
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for a in range(2,i):
                y = True
                if(i%a==0):
                    y = False
                    break
            if y:
                print(i)

# i really dont understand what is the palindromic number. because of this reason,
# i take this loop from the internet but i understand how it is created. thx


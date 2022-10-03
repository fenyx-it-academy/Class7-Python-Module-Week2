
#A palindromical prime number is a prime number that reads the same when reversed. 
#Write a function which returns the nearest palindromical prime number less than the multiplication of all the arguments.


#Example
#Input1>>>  some_function(2, 3, 4) 
#Output1>>>  the nearest palindromical prime number less than 24
#Input2>>> some_function(31, 77, 99)
#Output2>>> the nearest palindromical prime number less than 236,313


def plnd_prm (n1,n2,n3):
    x=0
    mult = n1*n2*n3
    for i in range(mult,1,-1):
        x=0
        for j in range (i-1,1,-1):
            if i%j == 0:
                x= 1
                break
        if x == 0:
            num_str = str(i)
            new = num_str[::-1]
            if num_str == new:
                print(i)
                break


num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter third number "))

plnd_prm(num1,num2,num3)
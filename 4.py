
# ### 4.
# A palindromical prime number is a prime number that reads the same when reversed. 
# Write a function which returns the nearest palindromical prime number less than 
# the multiplication of all the arguments.

# ```
# Example
# Input1>>>  some_function(2, 3, 4) 
# Output1>>>  the nearest palindromical prime number less than 24
# Input2>>> some_function(31, 77, 99)
# Output2>>> the nearest palindromical prime number less than 236,313
# ```
def nearst_pali_prime_num(*num):
    
    def is_prime ( num):
        if num%2==0 and num!=2 :
            return False
        for i in range (3,num,2):
            if num%i==0 :
                return False
        return True   


    def is_palindromical(num):
        string=str(num)
        str_list=list(string)
        str_list_rev= str_list.copy()
        str_list_rev.reverse()
        if str_list ==str_list_rev:
            return True
        return False
   
    multiply = 1
    for i in num:
        multiply*=i
    
    #now going backwards from our 'multiply' , checking every number if it is prim ? if yes > checking if it's palindromical
    #if yes, returning it
    print (multiply)
    if multiply%2==0 :  #if it is even : reducing it to the nearst odd, going 2 steps backwards (for better efficiency)
        multiply-=1
    for i in range ( multiply, 0, -2): #we made sure we are going to start with an odd num> thus we can jump 2 in every step
        if is_prime(i)   : 
           if  is_palindromical(i)  :
                    return i
    

print( nearst_pali_prime_num(11))
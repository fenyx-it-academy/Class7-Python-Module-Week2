def palindrome_prime(a,b,c):
    first = 1
    max_value = a * b * c
  
    for i in range(first,int(max_value)):
        if (str(i) == str(i)[::-1]): #checks if it is palindromical
            if(i>2):
                for j in range(2,i):
                    is_prime = True
                    if (i%j==0):
                        is_prime = False
                        break 
                if is_prime:
                    max_prime = i
        
    print(f"the nearest palindromical prime number less than {max_value} is ",max_prime)


    

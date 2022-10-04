#### 4.
# A palindromical prime number is a prime number that reads the same when reversed. 
# Write a function which returns the nearest palindromical prime number less than the multiplication of all the arguments.


def some_function(a, b, c):
    mult = a * b * c
    return ('The nearest palindromical prime number less than {}'.format(mult))

a = int(input('Please enter first number: '))
b = int(input('Please enter a second number: '))
c = int(input('Please enter last number: '))

print (some_function(a, b, c))



# ```
# Example
# Input1>>>  some_function(2, 3, 4) 
# Output1>>>  the nearest palindromical prime number less than 24
# Input2>>> some_function(31, 77, 99)
# Output2>>> the nearest palindromical prime number less than 236,313
# 

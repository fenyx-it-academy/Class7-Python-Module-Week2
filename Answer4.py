### 4.
# A palindromical prime number is a prime number that reads the same when reversed. 
# Write a function which returns the nearest palindromical prime number less than the multiplication of all the arguments.

# ```
# Example
# Input1>>>  some_function(2, 3, 4) 
# Output1>>>  the nearest palindromical prime number less than 24
# Input2>>> some_function(31, 77, 99)
# Output2>>> the nearest palindromical prime number less than 236,313

def nearest_palindromical_number(num: int):
  i = 0
  while True:
    small = num - i
    if str(small) == str(small)[::-1]:
      return(small)
    large = num + i
    if str(large) == str(large)[::-1]:
      return(large)
    i += 1
nearest_palindromical_number(100)
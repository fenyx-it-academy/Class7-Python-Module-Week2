def some_function(a, b, c):
    mult = a * b * c
    return ('The nearest palindromical prime number less than {}'.format(mult))

a = int(input('Please enter first number: '))
b = int(input('Please enter a second number: '))
c = int(input('Please enter last number: '))

print (some_function(a, b, c))


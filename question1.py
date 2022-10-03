num = int(input("Enter the number of the elements of the list: "))
k = int(input('Enter how many shifts you want? '
      '\nA positive number for right shifting and a negative number for left shifting: '))

my_list = (list(range(num)))
print(my_list)

if k > 0: #right shift
    for i in range(k):
        my_list.insert(0,my_list.pop())
elif k < 0: #left shift
    for i in range(abs(k)):
        my_list.append(my_list.pop(0))

print(my_list)
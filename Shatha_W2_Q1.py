"""Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

```
Example
Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3]
Inputs>>> [1, 2, 3, 4, 5], -2
Output>>> [3, 4, 5, 1, 2]
```"""
lst = []
lst2 = []
num = int(input('Enter number of elements'))
print('Enter the elements')
for i in range(0,num):
    ele = int(input())
    lst.append(ele) # adding the element

shift = int(input('Enter the number for shifting elements'))  

print(lst)

for i in range(0,num):
    j = i+shift
    if j < num:
        lst2.insert(j,lst[i])
    else:
        lst2.insert(j-num,lst[i])

print(lst2)
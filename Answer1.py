# ### 1.
# Write a program that takes two inputs; one of them is a list 
# and the other is a number, 
# and returns the list obtained by shifting the elements in the list n places to the right (left) 
# when n is positive (negative). 
# Use wrap-around: if an element is shifted beyond the end of the list, 
# then continue to shift starting at the beginning of the list.

# ```
# Example
# Inputs>>> [1, 2, 3, 4, 5], 2
# Output>>> [4, 5, 1, 2, 3]
# Inputs>>> [1, 2, 3, 4, 5], -2
# Output>>> [3, 4, 5, 1, 2]
# ```

# Python program to right rotate a list by n

# Returns the rotated list


def rotate_function(list, num):
    new_list =[]
    for i in range(len(list) - num, len(list)):
        new_list.append(list[i])
    for i in range(0, len(list) -num):
        new_list.append(list[i])

    return new_list


enter_list = input([]) 
enter_number = int(input())

rotate_function(enter_list, enter_number)




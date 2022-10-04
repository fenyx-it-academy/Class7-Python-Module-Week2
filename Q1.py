# ### 1.
# Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

# ```
# Example
# Inputs>>> [1, 2, 3, 4, 5], 2
# Output>>> [4, 5, 1, 2, 3]
# Inputs>>> [1, 2, 3, 4, 5], -2
# Output>>> [3, 4, 5, 1, 2]

def shiftfunction(mylist, mynumber):

    if 0<mynumber<len(mylist):
        
        return mylist[-1 * mynumber:] + mylist[:len(mylist) - mynumber]
    elif -1>mynumber> -1 * len(mylist):
        return mylist[len(mylist) + mynumber - 1:] + mylist[:mynumber - 1]
    else:
        return mylist




print(shiftfunction([1,2,3,4], 2))
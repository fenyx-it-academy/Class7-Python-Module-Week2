# ### 1.
# Write a program that takes two inputs; 
# one of them is a list and the other is a number,
#  and returns the list obtained by shifting the elements in the list n places to the right (left) 
# when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, 
# then continue to shift starting at the beginning of the list.

# ```
# Example
# Inputs>>> [1, 2, 3, 4, 5], 2
# Output>>> [4, 5, 1, 2, 3]
# Inputs>>> [1, 2, 3, 4, 5], -2
# Output>>> [3, 4, 5, 1, 2]
# ``

def shift(lis, num):
    """
      we are going to slice the list , depending on the number n : 
      if n =2 , we are going to slice the last two element , 
      put them in a 'slice list', and lastly add the last 3 elements of the original list  to them
    
    """
    slice_list=[]
    if num==0 or  num==len(lis) :
        return lis
    elif num==-1* len(lis) :
        return sorted(lis, reverse=True)
    elif num> len (lis):
        return lis
    elif num > 0 :
        slice_list=lis [-1*num:]
        
        return slice_list + lis[:len(lis)-num] 
    elif num < 0   : 
        slice_list=lis [:num-1]
        
        return   lis[len(lis)+num-1 :] + slice_list  
    
print (shift( [1, 2, 3, 4, 5] , 2)  )      



# Write a program that takes in two words as input and returns a list containing three elements, 
# in the following order:
# -		Shared letters between two words.
 	
# -		Letters unique to word 1.
 	
# -		Letters unique to word 2.

# Each element of the output should have unique letters, and should be alphabetically sorted. 
# Use set operations. The strings will always be in lowercase and will not contain any punctuation.
# ```
# Example
# Input1>>> "sharp"
# Input2>>> "soap"
# Output>>> ['aps', 'hr', 'o']
# ```
def Common_Uncommon_Words(str1, str2):
    l1 = []
    l2 = []
    l3 = []
    for i in str1:
        if (i in str2):
            l1.append(i)
        elif (i not in str2):
            l2.append(i)
    for j in str2:
        if (j not in str1):
                    l3.append(j)
    return [''.join(l1)] + [''.join(l2)] + [''.join(l3)]


print(Common_Uncommon_Words('sharp', 'soap'))
              
        
    
    
    

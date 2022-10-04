# ### 3.
# Write a program that takes in two words as input and returns a list containing three elements, in the following order:
# -		Shared letters between two words.
 	
# -		Letters unique to word 1.
 	
# -		Letters unique to word 2.

# Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. The strings will always be in lowercase and will not contain any punctuation.

# ```
# Example
# Input1>>> "sharp"
# Input2>>> "soap"
# Output>>> ['aps', 'hr', 'o']

def two_words(w1, w2):
    w1=set(w1)
    w2=set(w2)
    lis=[]

    lis.append  ("".join (sorted (w1& w2 ))  )
    lis.append  ("".join (sorted (w1- w2 ))  )
    lis.append  ("".join (sorted (w2-w1 ))  )

    return lis
print (two_words("sharp","soap")  )
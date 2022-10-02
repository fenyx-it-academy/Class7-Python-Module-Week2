
# ### 2.
# Write a code snippet that inputs a sentence from the user, then uses a dictionary to
#  summarize the number of occurrences of each letter. 
# Ignore case, ignore blanks and assume the user does not enter any punctuation.
#  Display a two-column table of the letters and their counts with the letters in sorted order.

# ```
# Example
# Input >>> "This is a sample text with several words This is more sample text with some different words"
# Output >>>
# [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
# ```
def count_dect(string):
    """this function takes a string an return a dictionary for every letter and its frequancy"""
    string=string.lower()
    
    dict={}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if string.count(letter) !=0 :
            dict[letter]= string.count(letter)
    return dict   
      
out=count_dect("This is a sample text with several words This is more sample text with some different words")
print (out)

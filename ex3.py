import string
lst=[]

word1 = set(input("please enter the first word: ").lower())
word2 = set(input("please enter the second word: ").lower())

sharedLetters = list(word1&word2)
uniquieWord1 = list(word1-word2)
uniquieWord2  = list(word2-word1)

 
#Sort list alphabetically and return list
sorted_sharedLetters = sorted(sharedLetters)
sorted_uniquieWord1 = sorted(uniquieWord1)
sorted_uniquieWord2 = sorted(uniquieWord2)


#Combine list elements into one string
sorted_sharedLetters_string = "".join(sorted_sharedLetters)
sorted_sorted_uniquieWord1 = "".join(sorted_uniquieWord1)
sorted_sorted_uniquieWord2 = "".join(sorted_uniquieWord2)


 



lst.append(sorted_sharedLetters_string)
lst.append(sorted_sorted_uniquieWord1)
lst.append(sorted_sorted_uniquieWord2)
print(lst)



 
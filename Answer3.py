
word1 = input()
word2 = input()
set1 = set(word1.lower())
set2 =  set(word2.lower())
lst1 = list(set1&set2)
lst2 = list(set1 - set2)
lst3 = list(set2 - set1)

print(f"{lst1} {lst2} {lst3}")
    
  
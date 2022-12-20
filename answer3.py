#collecting inputs:
word1 = set(input("type any word: ").lower())
word2 = set(input("type another word: ").lower())

#shared letters as a sorted string
common = sorted(set(word1 & word2))
incommon_str = ''.join (list (map (str, common)))

#Letters unique to word 1 as a sorted string:
unique_to1 = sorted(set(word1 - word2))
unique1 = ''.join (list (map (str, unique_to1)))

#Letters unique to word 2 as a sorted string:
uinque_to2 = sorted(set(word2 - word1))
unique2 = ''.join (list (map (str, uinque_to2)))

#creating a list of the above strings
lst = []
lst += [incommon_str]
lst +=[unique1]
lst +=[unique2]

# extracting the requested output: 
print("the output is:" + str(lst))




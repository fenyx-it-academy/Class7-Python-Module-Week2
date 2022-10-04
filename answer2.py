from collections import Counter

text = input('write a text! ')
d= text.replace(" ","")
letters=[i for i in d]
print(letters)
print(Counter(letters))

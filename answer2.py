import collections

sentence = input("type a sentence: ")


sentence = sentence.lower()
sentence = sentence.replace(" ","")

print(collections.Counter(sentence))

 
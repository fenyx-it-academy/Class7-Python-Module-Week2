import collections
from itertools import count


user_sentence = input("please enter your sentence: ")
user_sentence = user_sentence.lower()
my_dict = {}
dict_add = {}

for i in range(len(user_sentence)):
    if user_sentence[i] ==' ':
        continue
    letter_count =user_sentence.count( user_sentence[i])
    my_dict = { user_sentence[i] : letter_count }
    dict_add.update(my_dict)


sorted_dict_add = collections.OrderedDict(sorted(dict_add.items()))
print("\nletter \t number of occurances ")
for i in sorted_dict_add:
    print("{}\t{}".format(i,sorted_dict_add[i]))

 

 





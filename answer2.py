sentence = input('Please write a sentence: ')
sentence = sentence.replace(' ', '')

punc = """!()-[]{ };:'"\,<>./?@#$%^&*_~"""
new_form_sentence = ' '
dict = {}
for i in sentence:
    
    if i not in punc:
        new_form_sentence += i
    
    for keys in new_form_sentence:
        keys = keys.lower()
        keys = keys.strip()
            
    dict[keys] = dict.get(keys,0) + 1
    new_dict = list(zip(dict.keys(), dict.values()))

print(str(new_dict))

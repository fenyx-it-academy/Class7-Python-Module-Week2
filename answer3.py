def common(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    list1 = []
    list2 = []
    punc = """!()-[]{ };:'"\,<>./?@#$%^&*_~"""
    for i in str1:
        if i not in punc:
            list1 += i
    for i in str2:
        if i not in punc:
            list2 += i
    
    shared_letters = sorted(set(list1) & set(list2))
    unique_to_str1 = sorted(set(list1) - set(list2))
    unique_to_str2 = sorted(set(list2) - set(list1))

    return ' '.join (str(e) for e in shared_letters), ' '.join(str(e) for e in unique_to_str1), ' '.join(str(e) for e in unique_to_str2)
    

str1 = input('Please type a word: ')
str2 = input('Please type a second word: ')
print(common(str1, str2))

def extract_characters(sentence):
    sentence_list = list(sentence)
    ch_dict = {}
    for ch in set(sentence_list):
        ch_dict[ch] = sentence_list.count(ch)
    return ch_dict

sentence = 'This is a sample text with several words This is more sample text with some different words'
ch_dict = extract_characters(sentence)
print(ch_dict)

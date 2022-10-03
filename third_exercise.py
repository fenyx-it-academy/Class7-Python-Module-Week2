first_word = 'sharp'
second_word = 'soap'
first_word = set(first_word)
second_word = set(second_word)

output_list = []


output_list.append(sorted(first_word & second_word))
output_list.append(sorted (first_word - second_word))
output_list.append(sorted (second_word - first_word))
print(output_list)
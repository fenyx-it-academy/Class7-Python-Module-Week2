def shift_list(list_a, shift):
    return list_a[-shift:] + list_a[:-shift]


shifted_list = shift_list([1, 2, 3, 4, 5], -2)
print(shifted_list)
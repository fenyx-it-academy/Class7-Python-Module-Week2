import re

first = input("Enter the first word: ").lower().strip()
first = set(re.sub(r'[^\w\s]', '', first).replace(" ", ""))#remove the punctuations and blanks from the first word
second = input("Enter the second word: ").lower().strip()
second = set(re.sub(r'[^\w\s]', '', second).replace(" ", "")) #remove the punctuations and blanks from the second word

inters = first & second
f_diff = first - second
s_diff = second - first

print([''.join(inters), ''.join(f_diff), ''.join(s_diff)])


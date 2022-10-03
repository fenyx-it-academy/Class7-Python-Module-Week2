alphabet = "abcdefghijklmnopqrstuvwxyz"

sentence = input("Enter a sentence please: ").lower().strip()

result = {}
for letter in sentence:
    if letter in  alphabet:
        if letter in result.keys():
            result[letter] += 1
        else:
            result[letter] = 1


print([item for item in sorted(result.items())])
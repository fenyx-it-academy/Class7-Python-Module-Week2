def count_letters(text):
    result = {}
    text = text.lower()
    # Go through each letter in the text
    for i in text:
        # Check if the i needs to be counted or not
        if i.isalpha() :
            # Add or increment the value in the dictionary
            count = text.count(i)
            result[i] = count
    return result

print(count_letters("This is a sample text"))         

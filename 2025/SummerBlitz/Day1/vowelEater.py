# Prompt the user to enter a word
word = input("enter a word :")
# and assign it to the user_word variable.
user_word = word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A'or letter == 'E'or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)

print('That was ugly')

print('This is better:')

word_without_vowels = ""

# and assign it to the user_word variable.
user_word = word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A'or letter == 'E'or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter
# Print the word assigned to word_without_vowels.
print(word_without_vowels)
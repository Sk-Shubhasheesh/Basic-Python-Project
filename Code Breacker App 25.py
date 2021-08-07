# Hello, In the 25th challenge we create a Code Breaker App

from collections import Counter
print("Welcome to Code Breakers App")
# List of element to remove from all text for analysis
non_letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '.', '?', '!', ',', '"', "'", ':', ';', '(', ')', '%', '$', '&', '#', '\n', '\t']
# Comment out user input for key phrase 1
# Information for the first key key phrase_1
# key_phrase_1 = input("Enter a word or phrase to count the occurrence of each letter: ").lower().strip()
# Hard code of a pre.determined key phrase 1 for communication purpose
key_phrase_1 = """On the Insert tab, the galleries include items that are 
designed to coordinate with the overall look of your document. You can use
these galleries to insert tables, headers, footers, lists, cover pages, and 
other document building blocks. When you create pictures, charts, or 
diagrams, they also coordinate with your current document look.
You can easily change the formatting of selected text in the document text
by choosing a look for the selected text from the Quick Styles gallery on
the Home tab. You can also format text directly by using the other controls 
on the Home tab. Zoo is the like Zoo.
"""
key_phrase_1 = key_phrase_1.lower()
# Removing all non letters from key_phrase_1
for non_letter in non_letters:
    key_phrase_1 = key_phrase_1.replace(non_letter, '')

total_occurrences = len(key_phrase_1)

# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_1)
# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 1: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(percentage) + "%")
# Make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_1_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])
# Print the list
print("\nLetters ordered from highest occurrence to lower: ")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='' )

# Comment out user input for key phrase 1
# Information for the second key key phrase_2
# key_phrase_2 = input("\n\nEnter a word or phrase to count the occurrence of each letter: ").lower().strip()
# Removing all non letters from key_phrase_2
# Hard code of a pre.determined key phrase 1 for communication purpose
key_phrase_2 = """. Most controls offer a choice of using the look from the
current theme or using a format that you specify directly.To change the 
overall look of your document, choose new Theme elements on the Page Layout
tab. To change the looks available in the Quick Style gallery, use the
Change Current Quick Style Set command. Both the Themes gallery and the 
Quick Styles gallery provide reset commands so that you can always restore
the look of your document to the original contained in your current 
template. Z is also good.
"""
key_phrase_2 = key_phrase_2.lower()
for non_letter in non_letters:
    key_phrase_2 = key_phrase_2.replace(non_letter, '')

total_occurrences = len(key_phrase_2)
# Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)
# Determine the frequency analysis for the message
print("\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
    percentage = 100*value/total_occurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t\t" + str(value) + "\t\t\t" + str(percentage) + "%")
# Make a list of letters from highest occurrence to lowest
ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
    key_phrase_2_ordered_letters.append(pair[0])
# Print the list
print("\nLetters ordered from highest occurrence to lower: ")
for letter in key_phrase_2_ordered_letters:
    print(letter, end='')


# Encode/Decode a given message using  key_phrase_1 and  key_phrase_2
choice = input("\n\nWould you like to encode or decode a message: ").lower()
phrase = input("What is the phrase: ").lower()

# Removing all non letters from user phrase
for non_letter in non_letters:
    phrase = phrase.replace(non_letter, '')
# User wants to encode a message
if choice == 'encode':
    encoded_phrase = []
    for letter in phrase:
        index = key_phrase_1_ordered_letters.index(letter)
        letter = key_phrase_2_ordered_letters[index]
        encoded_phrase.append(letter)
    print("\nThe encoded message is: ")
    for letter in encoded_phrase:
        print(letter, end='')
# User wants to decode a message
elif choice == 'decode':
    decode_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
        letter = key_phrase_1_ordered_letters[index]
        decode_phrase.append(letter)
    print("\nThe decode message is: ")
    for letter in decode_phrase:
        print(letter, end='')

# User entered an invalid option
else:
    print("Please type 'encode' or 'decode'.  Try again.")





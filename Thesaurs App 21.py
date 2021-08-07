# Hello, In the 21th challenge we create a Thesaurus App
import random
# Define the Thesaurus
thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'fridge', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
    }

# Print welcome the Thesaurus app
print("Welcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you to synonym")
print("\nHere are the word in the Thesaurus")
for key in thesaurus.keys():
    print("\t-" + key)

# Get user input
choice = input("\nWhat word would you like a synonym for: ").lower().strip()

# Provide a random synonym
if choice in thesaurus.keys():
    index = random.randint(0,4)
    print("A synonym for " + choice + " is " + str(thesaurus[choice][index]) + ".")
else:
    print("I'm sorry, that word is not current in the thesaurus.")

# Get user input to see the whole Thesaurus
choice = input("\nWould you like to see the whole Thesaurus (yes/no): ").lower().strip()

# Shoe all value in the Thesaurus
if choice == 'yes':
    for key, values in thesaurus.items():
        print("\n" + key.title() + " synonyms are: ")
        for value in values:
            print("\t-" + value)
else:
    print("\nI hope you enjoyed the program.   Thank You!! ")



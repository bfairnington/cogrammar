"""Practical Task 1
Follow these steps:
● Create a file called alternative.py
● Write a program that reads in a string and makes each alternate
character into an upper case character and each other alternate character
a lower case character.
e.g. The string “Hello World” would become “HeLlO WoRlD”
● Now, try starting with the same string but making each alternative word
lower and upper case.
e.g. The string: “I am learning to code” would become “i AM learning
TO code”.
Tip: Using the split() and join() functions will help you here.
"""

# Alternate characters

# Input string
sentence = input("Enter a sentence")

# Create empty string
alternatechar = ""

# Enumerate string and assign upper or lower values depending on whether it is odd or even
for i in enumerate(sentence):
    if i[0] % 2 == 0:
        alternatechar += i[1].upper()
    
    else:
        alternatechar += i[1].lower()
    
# Print output
print(alternatechar)


# Alternate words

# Split sentence into list of words
sentencelist = sentence.split(" ")

# Create empty list
alternatelist = []

# Enumerate list and assign upper or lower values depending on whether it is odd or even 
for index, word in enumerate(sentencelist):
    if index % 2 == 0:
        alternatelist.append(word.lower())
    else:
        alternatelist.append(word.upper())

# Convert list back to sentence
alternateword = " ".join(alternatelist)

# Print output
print(alternateword)

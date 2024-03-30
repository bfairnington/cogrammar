# Practical Task 1

# Follow these steps:

# Create a new Python file called replace.py.

# Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a
# single string.

# Reprint this sentence as “The quick brown fox jumps over the lazy dog.”
# using the replace() function to replace every “!” exclamation mark with a
# blank space.

# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE
# LAZY DOG.” using the upper() function

# Print the sentence in reverse. (Hint: review what you learned about slicing!)

###############################################################################

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

print(sentence.replace("!", " "))

print(sentence.replace("!", " ").upper())

print(sentence[::-1])
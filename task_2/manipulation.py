# Practical Task 2

# Follow these steps:

# Create a new Python file in the Dropbox folder for this task, and call it
# manipulation.py.

# Ask the user to enter a sentence using the input() method. Save the user’s
# response in a variable called str_manip.

# Using this string value, write the code to do the following:
#   Calculate and display the length of str_manip.
#   Find the last letter in str_manip sentence. Replace every occurrence
#   of this letter in str_manip with ‘@’.
#       e.g. if str_manip = “This is a bunch of words”, the output would
#       be: “Thi@ i@ a bunch of word@”
#   Print the last 3 characters in str_manip backwards.
#       e.g. if str_manip = “This is a bunch of words”, the output would
#       be: “sdr”.
#   Create a five-letter word that is made up of the first three characters
#   and the last two characters in str_manip.
#       e.g. if str_manip = “This is a bunch of words”, the output
#       would be: “Thids”.

###############################################################################

str_manip = input("Input a sentence: ")

print(len(str_manip))

last_letter = str_manip[-1]
print(str_manip.replace(last_letter, "@"))

print(str_manip[:-4:-1])

five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)
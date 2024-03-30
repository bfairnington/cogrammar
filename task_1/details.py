# Practical Task 2

# Follow these steps:

# Create a new Python file in the Dropbox folder for this task, and call it
# details.py.

# As in practical task 1, please first provide pseudo code as comments in
# your Python file, outlining how you will solve this problem.

# Use an input() command to get the following information from the
# user.
#   Name
#   Age
#   House number
#   Street name

# Print out a single sentence containing all the details of the user.

# For example:
#   This is John Smith. He is 28 years old and lives at house
#   number 42 on Hamilton Street.

#############################################################################

# Use input command for each variable
name = input("Enter name: ")
age = input("Enter age: ")
house_number = input("Enter house number: ")
street_name = input("Enter street name: ")

# Print out all inputs in a single sentance
sentence = f"This is {name} who is {age} years old and lives at {house_number} {street_name}"

print(sentence)
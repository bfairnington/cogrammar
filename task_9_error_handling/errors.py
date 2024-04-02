""""
Practical Task 1
For both the errors.py and errors2.py task files in your folder, open the files and
follow these steps:
● Attempt to run the program. You will encounter various errors.
● Fix the errors and then run the program.
● Each time you fix an error, add a # comment in the line where you fixed it
and indicate which of the three types of errors it was with a brief
explanation of why that is.
● Save the corrected file.
"""

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Brackets added
print("\n") # Brackets added, indentation removed

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" # Remove indent, delete equaks sign, 
age = int(age_Str[:2]) # Remove indent, only use first 2 characters from variable "age_Str"
print("I'm " + str(age) + " years old.") # Remove indent, convert "age" into string, add spaces before and after "age"

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now) # Convert "years_from_now" into an integer

print("The total number of years:" + str(total_years)) # Add brackets to print function, rename "answer_years" to "total_years", remove quotation marks, convert "total_years" to string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Replace "years" with "total_years"
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Add bracket to print function, convert "total_months" to a string

#HINT, 330 months is the correct answer


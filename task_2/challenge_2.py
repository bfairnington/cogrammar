# Challenge 2

# Use this opportunity to extend yourself by completing an optional challenge
# activity.

# Let's practise some casting. Follow these steps:

#   Create a new file called challenge_2.py.
#   Write Python code to take the name of a user's favourite restaurant and
#   store it in a variable called string_fav.
#   Below this, write a statement to take in the user's favourite number. Use
#   casting to store it in an integer variable called int_fav.
#   Print out both of these using two separate print statements below what
#   you have written. Be careful!
#   Once this is working, try to cast string_fav to an integer. What happens?
#   Add a comment in your code to explain why this is.

###############################################################################

string_fav = input("What is your favourite restaurant? ")
int_fav = int(input("What is your favourite number? "))

print(string_fav)
print(str(int_fav))

# Non-numerical string cannot be cast as an integer
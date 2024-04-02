"""
Challenge
Use this opportunity to extend yourself by completing an optional challenge
activity.
Follow these steps:
● Create a new Python file called optional_challenge.py.
"""

# The following is an example of a logical error
num = int(input("Enter a non-zero number"))
    
while num == 0:
        num = int(input("Enter a non-zero number"))

num = 0
print(f"There is no problem with my logic. The number you entered was {num}")

# The following is an example of a runtime error
print("Any number divided by itself is 1. Let's test this out. Your number divded by itself is:")
selfdivision = num/num
print(selfdivision)

# The following are examples of syntax errors
print "This is a syntax error"
print(And this is another syntax error)

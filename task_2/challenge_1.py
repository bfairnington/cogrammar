# Challenge 1

# Use this opportunity to extend yourself by completing an optional challenge
# activity.

# Let’s try some slightly more complex maths. Follow these steps:

#   Create a new Python file in the Dropbox folder for this task, and call it
#   challenge_1.py.
#   Ask the user to enter the lengths of all three sides of a triangle.
#   Calculate the area of the triangle.
#   Print out the area.
#   Hints:
#       If side1, side2 and side3 are the sides of the triangle:
#           s = (side1 + side2 + side3)/2 and
#           area = √(s(s-a)*(s-b)*(s-c))
#       You’ll need to be able to calculate the square root (this may help)

###############################################################################

import math

side1 = float(input("Input length of traingle side 1: "))
side2 = float(input("Input length of traingle side 2: "))
side3 = float(input("Input length of traingle side 3: "))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
print(area)
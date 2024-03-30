# Practical Task 3

# Follow these steps:

# Create a new Python file called numbers.py.

# Ask the user to enter three different integers.

# Then print out:
#   The sum of all the numbers
#   The first number minus the second number
#   The third number multiplied by the first number
#   The sum of all three numbers divided by the third number

###############################################################################

int1 = int(input("Enter integer 1: "))
int2 = int(input("Enter integer 2: "))
int3 = int(input("Enter integer 3: "))

print(int1 + int2 + int3)
print(int1 - int2)
print(int3 * int1)
print((int1 + int2 + int3) / int3)
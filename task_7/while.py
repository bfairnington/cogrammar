"""
Follow these steps:
● Create a file called while.py.
● Write a program that continually asks the user to enter a number.
● When the user enters “-1”, the program should stop requesting the user
to enter a number,
● The program must then calculate the average of the numbers entered,
excluding the -1.
● Make use of the while loop repetition structure to implement the
program.
"""

i = 0
j = []

while i != -1:
    j.append(i)
    i = int(input("\nEnter a number:\n"))

j = j[1:]

average = sum(j) / len(j)
print(average)




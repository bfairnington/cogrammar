"""
Follow these steps:
● Create a new Python file in this folder called pattern.py.
● Write code to output the star pattern shown below, using an if-else
statement in combination with a single for loop (it’s really easy with two,
but using only one takes a little more thought!):
*
**
***
****
*****
****
***
**
*
"""

starsup = ""
starsdown = "*****"

for i in range(9):
    if len(starsup) < 5:
        starsup += "*"
        print(starsup)

    else:
        starsdown = starsdown[:len(starsdown)-1]
        print(starsdown)


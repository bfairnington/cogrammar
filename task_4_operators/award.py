# Practical Task 1

# Follow these steps:

# Create a new Python file in this folder called award.py.

# Design a program that determines the award a person competing in a
# triathlon will receive.

# Your program should read in the times (in minutes) for all three events of a
# triathlon, namely swimming, cycling, and running, and then calculate and
# display the total time taken to complete the triathlon.

# The award a participant receives is based on the total time taken to
# complete the triathlon. The qualifying time for awards is 100 minutes.
# Display the award that the participant will receive based on the following
# criteria:

# Qualifying Criteria           Time Range          Award

# Within the qualifying time.   0 - 100 minutes     Provincial Colours

# Within 5 minutes of the       101 - 105 minutes   Provincial Half
# qualifying time.                                  Colours 

# Within 10 minutes of the      106 - 110 minutes   Provincial Scroll
# qualifying time.

# More than 10 minutes off      111+ minutes        No award
# from the qualifying time.                    

###############################################################################

swimming = float(input("Input swimming time in minutes: "))
cycling = float(input("Input cycling time in minutes: "))
running = float(input("Input running time in minutes: "))

total = swimming + cycling + running

if total <= 100:
    print(f"Total time: {total} minutes\nAward: Provincial Colours")

elif total <= 105:
    print(f"Total time: {total} minutes\nAward: Provincial Half Colours")

elif total <= 110:
    print(f"Total time: {total} minutes\nAward: Provincial Scroll")

else:
    print(f"Total time: {total} minutes\nAward: None")
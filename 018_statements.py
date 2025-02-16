
# Statements
added = 2 + 3

# That statement uses the `=` operator to assign the result
# of the expression on the right (`2 + 3`) to the name on
# the left (`added`).
#
# It's called a statement because it changes the 'state' of
# the program.
#
# What's the state of a program? Let's take a look at an
# example.

my_favourite_number = 99

print(f"My favourite number is: {my_favourite_number}")
print("---")


# Here's the state of the above program after all lines are
# executed:
#
# | Name                | Value |
# | ------------------- | ----- |
# | my_favourite_number | 99    |
#
# We can refer to things in the state of the program by
# name.
#
# These names — `my_favourite_number` — are typically called
# 'variables'. This is because the names stay the same, but
# the values assigned to them can vary.
#
# Look at this program:

todays_day = 19
todays_day = 20

print(f"Today's day is: {todays_day}")
print("---")


from lib.helpers import check_that_these_are_equal

leaves_on_the_tree = 0

if leaves_on_the_tree == 0:
  print("It must be winter — or a dead tree")

if leaves_on_the_tree == 0:
  print("It must be winter — or a dead tree")
else:
  print("This is a happy tree with nice leaves")


# == Exercise One ==
print("")
print("Function: is_first_of_the_month")

def is_first_of_the_month(day_number):
  if day_number == 1:
    return "First of the month!"
  else: 
    return "Not first of the month"
 
 
check_that_these_are_equal(
  is_first_of_the_month(1),
  "First of the month!"
)

check_that_these_are_equal(
  is_first_of_the_month(12),
  "Not first of the month"
)

# == Exercise Two ==

print("")
print("Function: has_five_chars")

def has_five_chars(the_str):
  if len(the_str) == 5:
    return f"{the_str} is five characters long"
  else:
    return "Not five characters"

check_that_these_are_equal(
  has_five_chars("ABCDE"),
  "ABCDE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("FORGE"),
  "FORGE is five characters long"
)

check_that_these_are_equal(
  has_five_chars("Nope"),
  "Not five characters"
)

check_that_these_are_equal(
  has_five_chars("Nor this one"),
  "Not five characters"
)



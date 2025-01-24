from lib.helpers import check_that_these_are_equal


1 + 2 # evaluates to 3

1 == 2 # evaluates to False
2 == 2 # evaluates to True


def starts_with_x_or_y(the_str):
  first_letter = the_str[0]
  if first_letter == "x" or first_letter == "y":
    return "It does!"
  else:
    return "It does not."
  

# That `or` operator says "evaluate to true if the condition
# on the left, or on the right, or both evaluate to true".

print("")
print("Function: a_or_b")

def a_or_b(a, b):
  return a or b

check_that_these_are_equal(a_or_b(True, True), True)
check_that_these_are_equal(a_or_b(True, False), True)
check_that_these_are_equal(a_or_b(False, True), True)
check_that_these_are_equal(a_or_b(False, False), False)

# == Exercise One ==

print("")
print("Function: a_and_b")

def a_and_b(a, b):
  return a and b

check_that_these_are_equal(a_and_b(True, True), True)
check_that_these_are_equal(a_and_b(True, False), False)
check_that_these_are_equal(a_and_b(False, True), False)
check_that_these_are_equal(a_and_b(False, False), False)

# == Exercise Two ==

print("")
print("Function: not_a")

def not_a(a):
  return not a

check_that_these_are_equal(not_a(True), False)
check_that_these_are_equal(not_a(False), True)

x = 5
print(not(x > 3 and x < 10))


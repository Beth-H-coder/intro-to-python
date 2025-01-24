from lib.helpers import check_that_these_are_equal

def add_numbers(num1, num2):
    return num1 + num2

print("add_numbers(2, 3) is:")

check_that_these_are_equal(
  add_numbers(2, 3),
  5
)

print("add_numbers(3, 5) is:")

check_that_these_are_equal(
  add_numbers(3, 5),
  8
)


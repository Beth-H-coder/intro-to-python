from lib.helpers import check_that_these_are_equal


words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] 

for word in words:
  first_letter = word[0].upper() 
  first_letters.append(first_letter)
  # first_letters.append(first_letter.lower())

print(words)
print(first_letters)

# result = [word[0].upper() for word in words]
# print(result)

print("")
print("Function: add_one_hundred_to_numbers")

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
  new_nums = []
  for x in numbers:
    new_nums.append(x + 100)
  return new_nums

# def add_one_hundred_to_numbers(numbers):
#   return [number + 100 for number in numbers]

check_that_these_are_equal(
  add_one_hundred_to_numbers([1, 2, 3, 4]), [101, 102, 103, 104])
check_that_these_are_equal(
  add_one_hundred_to_numbers([2, 3, 4, 5]), [102, 103, 104, 105])


# -- list comprehension --

def add_one_hundred_to_numbers_2(numbers):
  new_nums = [x + 100 for x in numbers]
  return new_nums

print(add_one_hundred_to_numbers_2([2, 3, 4, 5]))


def square_nums(n):
  return [x ** 2 for x in range(0, n)]
  

check_that_these_are_equal(
  square_nums(5), [0, 1, 4, 9, 16])


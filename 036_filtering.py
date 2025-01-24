from lib.helpers import check_that_these_are_equal


raw_ages = [32, 40, None, 1, 32]

clean_ages = [] 

for age in raw_ages: 
  if age != None:
    clean_ages.append(age)

print(raw_ages)
print(clean_ages)


print("")
print("Function: only_positive_numbers")

# Return a new list with only the positive numbers
def only_positive_numbers(numbers):
  pos_nums = []
  for num in numbers:
    if num > 0:
      pos_nums.append(num)
  return pos_nums

check_that_these_are_equal(
  only_positive_numbers([-4, 4, -3, 3]), [4, 3])
check_that_these_are_equal(
  only_positive_numbers([-100]), [])


# Using list comprehension 
def only_pos_nums(numbers):
  return [num for num in numbers if num > 0]
  

print('list comp => ', only_pos_nums([6, 8, -4, -33, 20, -8, 901, -10001, 2]))

# A list comprehension that filters out odd numbers and squares the even numbers:
def squared_evens(list):
  return [num ** 2 for num in list if num % 2 == 0]

print(squared_evens([1, 2, 3, 6, 9, 10, 11, 12]))


# a = 10
# b = 15
# a = b
# print(a == b) # True
# print(a is b) # False





# Imagine someone didn't put their age in
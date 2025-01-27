from lib.helpers import check_that_these_are_equal
lines = [
  "My King,",
  "I need another five years.",
  "Then your crab will be ready.",
  "Sincerely,",
  "Chuang-tzu"
]

# text = "" 
# for line in lines: 
#   text = text + line 
#   text = text + "\n"

text = ""
for line in lines:
  text += line + "\n"

print(text)

another_text = "\n".join(lines)
print(another_text)

print("")


print("Function: add_up_numbers")

# Add up all the numbers in the list
def add_up_numbers(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

check_that_these_are_equal(
  add_up_numbers([1, 2, 3, 4]), 10)
check_that_these_are_equal(
  add_up_numbers([2, 3, 4, 5]), 14)

# -- using sum() -- 

def add_up_numbers_2(numbers):
  return sum(numbers)

print(add_up_numbers_2([5, 6, 7, 8, 9, 120])) # 155


# -- using a while -- 

def add_up_with_a_while(numbers):
  i = 0
  total = 0
  while i < len(numbers):
    total += numbers[i]
    i += 1
  return total

add_up_with_a_while([5, 6, 7, 8, 9, 120])

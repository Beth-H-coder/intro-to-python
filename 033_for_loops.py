
for letter in ["a", "b", "c"]:
  print(f"This letter is {letter}")

print("- - - range - -  -")

def print_numbers_in_range():
  for number in range(0, 10):
    print(f"This number is {number}")

print_numbers_in_range()

print("- - - with a while - -  -")

def print_numbers_in_range_with_a_while():
  number = 0
  while number < 10:
    print(f"This number is {number}")
    number = number + 1


print_numbers_in_range_with_a_while()

# loop over indices of list using range() and len()

def create_string_and_dict(list):
  new_str = ""
  my_dict = {}
  for i in range(len(list)):
    print(i)
    new_str += list[i] + " "
    my_dict[i] = list[i]
    print(i, list[i])
  print(new_str)
  print(new_str[:-1] + '.')    
  return my_dict

print(create_string_and_dict(['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']))


def count_in_increments(num):
  for x in range(0, 10, num):
    print(x)
  
count_in_increments(3)


def count_in_decrements(num):
  for x in range(10, 0, num):
    print(x)

count_in_decrements(-2)
# * Summarising: Using a loop to distil a list into one
#   value.

# * Mapping: Using a loop to convert each item to another
#   item.

# * Filtering: Using a loop to pick out only some items from
#   a list.


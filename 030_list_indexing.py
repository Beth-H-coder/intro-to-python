from lib.helpers import check_that_these_are_equal

my_list = [44, 35, 21, 63, 27, 4, 22]
my_list[0]   # Evaluates to 44
my_list[-1]  # Evaluates to 22
my_list[1:3] # Evaluates to [35, 21]
print(my_list[0]) # 44
print(my_list[-1]) # 22
print(my_list[1:3]) #[35, 21]
print(my_list[:3]) # [44, 35, 21]
print(my_list[4:]) # [27, 4, 22]
print(my_list[-3:-2]) # [27]
# == Exercise One ==

print("Function: get_first_item")

def get_first_item(the_list):
  return the_list[0]

check_that_these_are_equal(
  get_first_item(["a", "b", "c", "d", "e"]),
  "a"
)
check_that_these_are_equal(
  get_first_item([34, 44, 54, 64]),
  34
)
# == Exercise Two ==

print("Function: get_last_item")

def get_last_item(the_list):
  return the_list[-1]

check_that_these_are_equal(
  get_last_item(["a", "b", "c", "d", "e"]),
  "e"
)

check_that_these_are_equal(
  get_last_item([34, 44, 54, 64]),
  64
)

# == Exercise Three ==

print("")
print("Function: get_nth_item")

def get_nth_item(the_list, n):
  return the_list[n]

check_that_these_are_equal(
  get_nth_item(["a", "b", "c", "d", "e"], 3),
  "d"
)

check_that_these_are_equal(
  get_nth_item([34, 44, 54, 64], 1),
  44
)

# == Exercise Four ==

print("")
print("Function: get_items_between_one_and_three")

def get_items_between_one_and_three(the_list):
  return the_list[1:3]

check_that_these_are_equal(
  get_items_between_one_and_three(["a", "b", "c", "d", "e"]),
  ["b", "c"]
)

check_that_these_are_equal(
  get_items_between_one_and_three([34, 44, 54, 64]),
  [44, 54]
)


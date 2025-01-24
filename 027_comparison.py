from lib.helpers import check_that_these_are_equal

print("")
print("Function: a_is_equal_to_b")

def a_is_equal_to_b(a, b):
  return a == b

check_that_these_are_equal(
  a_is_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_equal_to_b("a", "a"),
  True
)

check_that_these_are_equal(
  a_is_equal_to_b(1, 2),
  False
)

# == Exercise One ==
print("")
print("Function: a_is_less_than_b")

def a_is_less_than_b(a, b):
  return a < b
  
check_that_these_are_equal(
  a_is_less_than_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_less_than_b(2, 1),
  False
)

# == Exercise Two ==

print("")
print("Function: a_is_greater_than_b")

def a_is_greater_than_b(a, b):
  return a > b
  

check_that_these_are_equal(
  a_is_greater_than_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_greater_than_b(2, 1),
  True
)

# == Exercise Three ==

print("")
print("Function: a_is_less_than_or_equal_to_b")

def a_is_less_than_or_equal_to_b(a, b):
  return a <= b
  

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_less_than_or_equal_to_b(2, 1),
  False
)

# == Exercise Four ==

print("")
print("Function: a_is_greater_than_or_equal_to_b")

def a_is_greater_than_or_equal_to_b(a, b):
 return a >= b
  

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 2),
  False
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(1, 1),
  True
)

check_that_these_are_equal(
  a_is_greater_than_or_equal_to_b(2, 1),
  True
)

# == Exercise Five ==

print("")
print("Function: a_is_not_equal_to_b")

def a_is_not_equal_to_b(a, b):
  return a != b
  

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 2),
  True
)

check_that_these_are_equal(
  a_is_not_equal_to_b(1, 1),
  False
)

check_that_these_are_equal(
  a_is_not_equal_to_b(2, 1),
  True
)

# == Exercise Six ==

print("")
print("Function: a_is_within_b")

def a_is_within_b(a, b):
  return a in b

check_that_these_are_equal(
  a_is_within_b("e", "hello"),
  True
)

check_that_these_are_equal(
  a_is_within_b("f", "hello"),
  False
)

txt = "The rain in Spain falls mainly on the plain"
is_present = 'rain' in txt
print(is_present)


is_present_2 = 'brain' in txt
print(is_present_2)


is_not_present = 'England' not in txt
print(is_not_present)

my_dict = { 'a': 1, 'b': 2, 'c': 3}
print('b' in my_dict)

my_dict_with_num_keys = { 1: 'a', 2: 'b', 3: 'c'}
print('b' in my_dict_with_num_keys)

my_dict_with_num_keys_2 = { 1: 'a', 2: 'b', 3: 'c'}
print(3 in my_dict_with_num_keys)
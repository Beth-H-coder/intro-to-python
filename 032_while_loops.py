from lib.helpers import check_that_these_are_equal

my_name = "Kay"
if my_name == "Kay":
  print("Hello, Kay!")
else:
  print("Hello, you!")


i = 0 
while i < 10:
  print(f"The number is now {i}")
  i = i + 1


print("")
print("Function: add_cats_repeatedly")

def add_cats_repeatedly(word_list, count):
  i = 0
  while i < count:
    word_list.append('cats')
    i = i + 1
  return word_list

check_that_these_are_equal(
  add_cats_repeatedly([], 3), ['cats', 'cats', 'cats'])
check_that_these_are_equal(
  add_cats_repeatedly(['dogs'], 2), ['dogs', 'cats', 'cats'])









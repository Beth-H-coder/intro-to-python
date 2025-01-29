from lib.helpers import check_that_these_are_equal

my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list) # my_list is now ["a", "b", "c", "d"]

my_num = 3
my_num + 1
print(my_num) # my_num is still 3

my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list) # my_list is now ["a", "b", "c", "d"]

my_list = ["a", "b", "c"]
my_copy = my_list.copy()
my_copy.append("d")
print(my_list) # my_list is still ["a", "b", "c"]
print(my_copy) # my_copy is now   ["a", "b", "c", "d"]

print("")
print("Function: append_item_to_list")

def append_item_to_list(the_list, item):
  res = the_list.append(item)
  print('res =>', the_list)
  return the_list

check_that_these_are_equal(
  append_item_to_list(['a', 'b'], 'c'), ['a', 'b', 'c'])
check_that_these_are_equal(
  append_item_to_list([3, 1], 6), [3, 1, 6])

# == Exercise One ==

print("")
print("Function: remove_item_from_list")

def remove_item_from_list(the_list, item):
  the_list.remove(item)
  return the_list

check_that_these_are_equal(
  remove_item_from_list(['a', 'b'], 'b'), ['a'])
check_that_these_are_equal(
  remove_item_from_list([3, 1], 3), [1])

# == Exercise Two ==

print("")
print("Function: count_items_in_list")

def count_items_in_list(the_list, item):
  return the_list.count(item)

check_that_these_are_equal(
  count_items_in_list(['a', 'b', 'a'], 'a'), 2)
check_that_these_are_equal(
  count_items_in_list([4, 1, 4, 4], 4), 3)

# == Exercise Three ==

print("")
print("Function: get_index_of_item")

def get_index_of_item(the_list, item):
  return the_list.index(item)

check_that_these_are_equal(
  get_index_of_item(['a', 'b', 'c'], 'b'), 1)
check_that_these_are_equal(
  get_index_of_item([33, 44, 55], 55), 2)

# == Exercise Four ==

print("")
print("Function: reverse_list")

def reverse_list(the_list):
  the_list.reverse()
  return the_list

check_that_these_are_equal(
  reverse_list(['a', 'b', 'c']), ['c', 'b', 'a'])
check_that_these_are_equal(
  reverse_list([33, 44, 55]), [55, 44, 33])

# == Exercise Five ==

print("")
print("Function: list_length")

# Note — it's the same as for strings!
def list_length(the_list):
  return len(the_list)

check_that_these_are_equal(
  list_length(['a', 'b', 'c']), 3)
check_that_these_are_equal(
  list_length([33, 44]), 2)



#  https://docs.python.org/3/tutorial/datastructures.html

# names_list = ['tom', 'fran', 'beth', 'anne', 'florence']
# names_list.remove('charlotte')
# print(names_list) # error 

names = ['beth', 'fran', 'tom', 'jim', 'florence', 'lucy', 'fran']
names2 = ['beth', 'fran', 'tom', 'jim', 'florence', 'lucy', 'fran']


def remove_item(my_list, item):
    my_list.remove(item)
    return my_list
   

def remove_item_with_check(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list
    

print('------------------')
# when item to remove present in list 
remove_item(names, 'fran' )
print('remove_item =>', names)

remove_item_with_check(names2, 'fran' )
print('remove_item_with_check =>', names2)

# when item to remove not present 

# remove_item(names, 'anna' )
# print(names) # error as 'anna' not in array 

names2 = ['beth', 'fran', 'tom', 'jim', 'florence', 'lucy', 'fran']
remove_item_with_check(names2, 'anna')
print(names2)


print('--- remove all occurrences ----')

# def off_the_list(list, item_to_exclude):
#   new_list = []
#   for x in list:
#      if x != item_to_exclude:
#         new_list.append(x)
#   return new_list

def off_the_list(list, item_to_exclude):
   return [item for item in list if item != item_to_exclude]
   




# def off_the_list(list, item_to_exclude):
#    return [item.upper() if item.startswith('o') else item for item in list if item != item_to_exclude]

print('test off list', off_the_list(['benji', 'oscar', 'leo', 'pop', 'benji', 'shivers', 'stella', 'benji'], 'benji'))

my_list = [30, 10, 20, 30, 40, 50]
index = my_list.index(30, 1, 4)  # Searches for 30 between index 1 and 4
print(index)  # Output: 2


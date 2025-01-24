
example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

def generate_frequency_graph(numbers):
  integers = get_only_integers(numbers)
  positive_integers = convert_negatives_to_positives(integers)
  number_frequency = calc_frequency_of_numbers(positive_integers)
  graph = format_graph(number_frequency)
  return graph

def get_only_integers(numbers):
  integers = []
  for number in numbers:
    if number != None:
      integers.append(number)
  return integers

# def convert_negatives_to_positives(numbers):
#   positive_integers = []
#   for number in numbers:
#     if number < 0:
#       positive_integers.append(number * -1)
#     else:
#       positive_integers.append(number)
#   return positive_integers

# using abs() - returns absolute value of a number
#  
def convert_negatives_to_positives(numbers):
  positive_integers = []
  for number in numbers:
    positive_integers.append(abs(number))
  return positive_integers

def calc_frequency_of_numbers(numbers):
  number_frequency = {}
  for number in numbers:
    if number not in number_frequency:
      number_frequency[number] = 1
    else:
      number_frequency[number] += 1
  print(number_frequency)
  return number_frequency

def format_graph(number_frequency):
  graph = ""
  for number in number_frequency:
    graph += f"{number}: {'x' * number_frequency[number]}\n"
  return graph

print(generate_frequency_graph(example_numbers))


# create dictionary with Counter 
from collections import Counter

numbers_list = [1, 2, 2, 3, 3, 3]
counts = Counter(numbers_list)

print(counts)  # Output: Counter({3: 3, 2: 2, 1: 1})

#  create dictionary with set - dictionary comprehension 
numbers_list_2 = [1, 2, 2, 3, 3, 3]
counts_2 = {num: numbers_list_2.count(num) for num in set(numbers_list_2)}

print(counts_2)  # Output: {1: 1, 2: 2, 3: 3}

print('--- play around')
test_dict = {1: 5, 2: 3, 4: 9, 4: 1, 5: 2}
# 1: *****
# 2: ***
# ['hi', 'i', 'am', 'fran']
for key, value in test_dict.items():
  print(key)
  print(value)
# my_str = '\n'.join(test_dict)

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

# loop through dictionary with items() and dictionary comprehension and create a string with each element on a new line

test_dict = {1: 5, 2: 3, 4: 9, 6: 6, 5: 2}

my_str = '\n'.join(f"{key}: {value * 'x'}" for key, value in test_dict.items())
print(my_str)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

print(thisdict.items())






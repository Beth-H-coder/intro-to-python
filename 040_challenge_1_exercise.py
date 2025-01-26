from lib.helpers import check_that_these_are_equal

print("Function: report_long_words")

# Solution 1
# def report_long_words(words):
#   unhyphenated = remove_hyphens(words)
#   long_words = get_long_words(unhyphenated)
#   report = format_string(long_words)
#   return report

# def remove_hyphens(words):
#   return [word for word in words if '-' not in word]

# def get_long_words(words):
#   return [word[:15] + "..." if len(word) > 15 else word for word in words if len(word) > 10]

# def format_string(words):
#   new_str = ', '.join(words) 
#   return f"These words are quite long: {new_str}"


# Solution 2: with more functions
# def report_long_words(words):
#   long_words = get_long_words(words)
#   unhyphenated = remove_hyphens(long_words)
#   shortened_if_longer = truncate_words(unhyphenated)
#   report = format_string(shortened_if_longer)
#   return report

# def get_long_words(words):
#   return [word for word in words if len(word) > 10]

# def remove_hyphens(hyphenated_words):
#   return [word for word in hyphenated_words if '-' not in word]

# def truncate_words(words):
#   return [word[:15] + '...' if len(word) > 15 else word for word in words]

# def format_string(words):
#   new_str = ', '.join(words) 
#   return f"These words are quite long: {new_str}"
  
# Solution 3 - hyphenated and long words of > 10 combined 

def report_long_words(words):
    unhyphenated_long_words = get_unhyphenated_and_longer_than_10(words)
    processed_and_shortened = shorten(unhyphenated_long_words)
    report = format_string(processed_and_shortened)
    return report

def get_unhyphenated_and_longer_than_10(words):
    return [word for word in words if len(word) > 10 and '-' not in word]

def shorten(words):
    return [word[:15] + '...' if len(word) > 15 else word for word in words]

def format_string(words):
    new_str = ', '.join(words)
    return f"These words are quite long: {new_str}"


# Solution 4 - 
# def report_long_words (words):
#   unhyphenated = remove_hyphens(words)
#   long_words = get_long_words(unhyphenated)
#   report = format_string(long_words)
#   return report

# def remove_hyphens(words):
#   unhyphenated_words = []
#   for word in words:
#     if '-' not in word:
#       unhyphenated_words.append(word)
#   return unhyphenated_words

# def remove_hyphens(words):
#   return [word for word in words if '-' not in word]

# print('test remove_hyphens =>', remove_hyphens(['one', 'antidisestablishmentarianism', 'half-hearted', 'father-in-law', 'frances', 'supercalifragilisticexpialidocious', 'free-range', 'good-looking', 'beth']))

# for loop solution 
# def get_long_words(words):
#   long_words = []
#   for word in words:
#     if len(word) > 10:
#       if len(word) > 15:
#         shortened_word = word[:15] + '...'
#         long_words.append(shortened_word)
#       else:
#         long_words.append(word)
#   return long_words

# def get_long_words(words):
#   return [word[:15] + "..." if len(word) > 15 else word for word in words if len(word) > 10]

# print('test get_long_words =>', get_long_words(['one', 'sponsorship', 'antidisestablishmentarianism', 'frances', 'supercalifragilisticexpialidocious', 'beth', 'prestigious']))


# def format_string(words):
#   new_str = ', '.join(words) 
#   return f"These words are quite long: {new_str}"

# print('test format_string =>', format_string(['sponsorship', 'antidisestablis...', 'supercalifragil...', 'prestigious']))

print('report_long_words =>', report_long_words([  'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism']))


check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)



# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."
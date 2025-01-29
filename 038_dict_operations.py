from lib.helpers import check_that_these_are_equal

text = "the quick brush jumped over the lazy crabbbbbbb"

letter_counts = {}

for letter in text:
  if letter not in letter_counts:
    letter_counts[letter] = 1
  else:
    letter_counts[letter] += 1

print('letter counts => ', letter_counts)
# get the letter with the highest value
highest = None
for x in letter_counts:
  if highest is None or letter_counts[x] > letter_counts[highest]:
    highest = x

print('This is the most common character =>', highest)

print("")
print("Function: count_words_by_length")

def count_words_by_length(words):
  count = {}
  for word in words:
    if len(word) not in count:
      count[len(word)] = 1
    else:
      count[len(word)] += 1
  print(count)
  return count 

check_that_these_are_equal(
  count_words_by_length(["hat", "cat", "I", "bird"]),
  {3: 2, 1: 1, 4: 1}
)

check_that_these_are_equal(
  count_words_by_length(["four", "four", "four", "one"]),
  {4: 3, 3: 1}
)

from collections import Counter 

thislist = [1, 3, 4, 3, 3, 3, 6, 8, 4, 3, 3, 3, 7, 7, 3, 1, 2]

numcount = Counter(thislist)
print(numcount)
print(numcount[3])
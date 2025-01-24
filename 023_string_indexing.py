from lib.helpers import check_that_these_are_equal

note = "The Most Perfect Crab"
print(note)
print(note[0])

print(note[-1])

print(note[6])

print(note[0:3])

print(note[:8])
print(note[17:])



# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(the_str):
  return the_str[0]

check_that_these_are_equal(
  get_first_letter("The king granted them"),
  "T"
)
check_that_these_are_equal(
  get_first_letter("Five years later"),
  "F"
)

# == Exercise Two ==

print("Function: get_last_letter")

def get_last_letter(the_str):
  return the_str[-1]
 
check_that_these_are_equal(
  get_last_letter("The king granted them"),
  "m"
)
check_that_these_are_equal(
  get_last_letter("Five years later"),
  "r"
)

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(the_str, n):
  return the_str[n]

check_that_these_are_equal(
  get_nth_letter("The king granted them", 4),
  "k"
)
check_that_these_are_equal(
  get_nth_letter("Five years later", 7),
  "a"
)

# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(the_str):
  return the_str[4:8]

check_that_these_are_equal(
  get_letters_between_four_and_eight("The king granted them"),
  "king"
)
check_that_these_are_equal(
  get_letters_between_four_and_eight("Five years later"),
  " yea"
)

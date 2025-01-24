from lib.helpers import check_that_these_are_equal

length = len("Hello!")
print(f"The string is {length} characters long")

old_string = "Hello, YOUR_NAME!"
new_string = old_string.replace("YOUR_NAME", "Kay")
print(new_string)

my_string = "hello"

len(my_string)             
my_string.replace("h", "w") 

# == Exercise One ==

print("")
print("Function: uppercase")

def make_uppercase(string):
  return string.upper()
  

check_that_these_are_equal(
  make_uppercase("hello"), "HELLO")

check_that_these_are_equal(
  make_uppercase("World"), "WORLD")

# == Exercise Two ==
print("")
print("Function: lowercase")

def make_lowercase(string):
  print(string.lower())
  return string.lower()
  
check_that_these_are_equal(
  make_lowercase("HELLO"), "hello")

check_that_these_are_equal(
  make_lowercase("World"), "world")

# == Exercise Three ==
print("")
print("Function: strip_whitespace")

def strip_whitespace(string):
  res = string.strip()
  print(res)
  return res

check_that_these_are_equal(
  strip_whitespace("hello "), "hello")

check_that_these_are_equal(
  strip_whitespace(" hello world "), "hello world")



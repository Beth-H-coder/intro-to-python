from lib.helpers import check_that_these_are_equal
my_string = "Ant" + "eater"
print(my_string)

# my_string = "Forty" + 2
my_string = "Forty" + str(2)
print(my_string)

my_name = "Kay"
print(f"Hello, {my_name}!")

print(f"Your name is {len(my_name)} characters long")

# == Exercise One ==
print("")
print("Function: greet")

def greet(name):
	return f"Hello, {name}!"

check_that_these_are_equal(
	greet("Chuang-tzu"),
	"Hello, Chuang-tzu!"
)

check_that_these_are_equal(
	greet("Crab"),
	"Hello, Crab!"
)

print("Forty" + str(2)) # Forty2
print(1 + int("1")) #2
x = 1 + int(1)
print(type(x))
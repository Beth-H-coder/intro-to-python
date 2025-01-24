
def add_one(num):
  return num + 1

# | Code           | What is it?                                        |
# | -------------- | -------------------------------------------------- |
# | def            | `def` is a keyword that defines a new function     |
# | add_one        | `add_one` is the function name                     |
# | (num)          | `(num)` is the parameter list                      |
# | num            | `num` is a parameter                               |
# | :              | The `:` symbol indicates the body should start now |
# | return num + 1 | `return num + 1` is a statement                    |
# | num + 1        | `num + 1` is an expression                         |
# | num            | `num` here is a variable                           |
# | +              | `+` is an operator                                 |
# | 1              | `1` is a literal number                            |

# Operators, statements, and expressions. 

# Operators

# To be a great programmer you will have to become a
# great researcher. 
#
# 1. Search the web for "Python operators", to
# 2. Find and fill out the following list of operators.

# Addition
added = 2 + 3
print(f"2 + 3 = {added} (should be 5)")

# Multiplication
multiplied = 2 * 3
print(f"2 * 3 = {multiplied} (should be 6)")

# == Subtraction ==
subtracted = 2 - 3
print(f"2 - 3 = {subtracted} (should be -1)")

# == Division ==
divided = 2 / 3
print(f"2 / 3 = {divided} (should be 0.6666666666666666)")

# == Modulus ==
modulus = 3 % 2
print(f"3 % 2 = {modulus} (should be 1)")

# == Floor division ==
floor_divided = 2 // 3
print(f"2 // 3 = {floor_divided} (should be 0)")

# == Exponentiation ==
# Sometimes known as "2 to the power of 3"
expr = 2 ** 3
print(f"2 ** 3 = {expr} (should be 8)")

x = 5
x += 3
print(x) # 8

x = 5
x%=3
# x = x % 3 
print(x) # 2

x = 5 # Binary is base -2 using only 0 and 1: 
# 5 / 2 = 2 remainder 1, 
# 2 (from previous) / 2 = 1, 
# 1 (from previous) / 2 = 0, remainder 1
# Bottom-up remainders - 101
x &= 3
# 3 / 2 = 1, remainder 1
# 1 / 2 = 0, renainder 1
# Bottom-up remainders - 11 or 011 with 0 in front 
print(x)
# 5 in binary: 101
# 3 in binary: 011
# Both bits are 1 - result is 1
# Otherwise result is 0


def is_odd(num):
  return num % 2 == 1

def is_even(num):
  return num % 2 == 0

print(is_odd(11)) # True 
print(is_odd(12)) # False
print(is_even(11)) # False 
print(is_even(12)) # True

# Expressions 

added = 2 + 3

# The expression is the fundamental unit of computation in your program. 
#  It is the combination of data and operators (and some other things) to produce a result.

# Here are some more examples of expressions:

2            # Evaluates to: 2
2 + 3        # Evaluates to: 5
2 * 3        # Evaluates to: 6
2 + 3 * 4    # Evaluates to: 14


# Run `python` in your shell and type that code into it. 
# >>> 2 + 3
# Type in 'exit()' to leave Python.
# So we get 14! Python executes the multiplication first, and then the addition. 
# We can control this using brackets.

(2 + 3) * 4 # 20

# We can use brackets to control the order in which the expressions are evaluated.

# Python REPL
# Read, Evaluate, and Print Loop.
# Reads the code you type in, evaluates the expression, prints the result,
# and then does that forever in a loop.
#
# You can use it to find out what different expressions evaluate to

def add_one(num):
  return num + 1

# Here are some more expressions:

add_one(2)          # Evaluates to 3
add_one(3)          # Evaluates to 4
add_one(4) * 3      # Evaluates to 15
2 + add_one(4) * 3  # Evaluates to 17

# What to take from this? Calling a function is also an expression! Many things in Python
# are expressions, and we can combine data, operators, and function calls into some very
# advanced expressions.

# Run: python -i 017_expressions.py and then type in some of the above expressions.
#
# The `-i` flag means 'open a REPL that can use the code in this file'
# add_one(9) + 2 * 3 # 16

add_one(add_one(add_one(add_one(add_one(add_one(1)))))) # 7
# Calling a function
def greet(name):
    print(f"Hi {name}")
greet('John')

# Returning a value
def greet(name):
    return f"Hi {name}"
greeting = greet('John')
print(greeting)

# Python functions with multiple parameters
def sum(a, b):
    return a + b
total = sum(10,20)
print(total)

# recursive functions
def count_down(start):
    """ Count down from a number  """
    print(start)
    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)

count_down(3)
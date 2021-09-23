# pass function as parameter
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)
def first_last(first_name, last_name):
    return f"{first_name} {last_name}"
def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"
full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe
full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John


# lambda expression
def get_full_name2(first_name, last_name, formatter):
    return formatter(first_name, last_name)
full_name = get_full_name2('John', 'Doe', lambda first_name, last_name: f"{first_name} {last_name}")
print(full_name)
full_name = get_full_name2('John', 'Doe', lambda first_name, last_name: f"{last_name} {first_name}")
print(full_name)
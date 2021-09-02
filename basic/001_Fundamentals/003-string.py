message = 'This is a string in Python'
message = "This is also a string"
message = "It's a string"
message = '"Beautiful is better than ugly.". Said Tim Peters'
message = 'It\'s also a valid string'
message = r'C:\python\bin'
help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
print(help_message)

# Using variables in Python strings with the f-strings
name = 'John'
message = f'Hi {name}'
print(message)

# Concatenating Python strings
greeting = 'Good ' 'Morning!'
print(greeting)

greeting = 'Good '
time = 'Afternoon'
greeting = greeting + time + '!'
print(greeting)

#Accessing string elements
str = "Python String"
print(str[0]) # P
print(str[1]) # y

str = "Python String"
print(str[-1])  # g
print(str[-2])  # n

#Getting the length of a string
str = "Python String"
str_len = len(str)
print(str_len)

#Slicing strings
str = "Python String"
print(str[0:2])

#Python strings are immutable
str = "Python String"
new_str = 'J' + str[1:]
print(new_str)
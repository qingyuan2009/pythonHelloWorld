
#Uses the int() function to convert the input strings to numbers
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')

print(type(100))  #<class 'int'>
print(type(2.0))  #<class 'float'>
print(type('Hello'))  #<class 'str'>
print(type(True))  #<class 'bool'>


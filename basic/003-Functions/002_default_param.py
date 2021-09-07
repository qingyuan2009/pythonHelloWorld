#Python default parameters example
def greet(name, message='Hi'):
    return f"{message} {name}"

greeting = greet('John', 'Hello')
print(greeting)
greeting = greet('John')
print(greeting)

#keyword arguments
def get_net_price(price, discount):
    return price * (1-discount)
net_price = get_net_price(price=100, discount=0.1)
print(net_price)
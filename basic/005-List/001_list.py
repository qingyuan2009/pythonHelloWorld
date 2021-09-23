empty_list = []

todo_list = ['Learn Python List','How to manage List elements']
print(todo_list)

numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
print(numbers[0])         # index
print(numbers[-2])        # 9 --> count backwards
numbers.append(100)       # append to the end
print(numbers)
numbers.insert(2, 99)     # insert in between
print(numbers)
del numbers[0]            # delete
print(numbers)

numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()            # pop: remove the last and return that element
second = numbers.pop(1)
print(last)
print(second)
print(numbers)

numbers = [1, 3, 2, 7, 9, 4]
numbers.remove(9)               # remove
print(numbers)

coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)
for index in range(0, 10):
    print(index)
    if index == 3:
        break

for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")

for index in range(10):
    if index % 2:
        continue
    print(index)
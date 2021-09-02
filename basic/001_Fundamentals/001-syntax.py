import keyword

# define main function to print out something
def main():
    # Whitespace and indentation
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

    # IF statement
    a = True
    b = False
    c = True
    if (a == True) and (b == False) and \
            (c == True):
        print("Continuation of statements")

    # print key word list, import keyword first
    print(keyword.kwlist)

    # String literals
    s = 'This is a string'
    print(s)
    s = "Another string using double quotes"
    print(s)
    s = ''' string can span
            multiple line '''
    print(s)

# call function main
main()
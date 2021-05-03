a = int(input('Enter the first Number: '))
b = int(input('Enter the second Number: '))
c = int(input('Enter the third Number: '))

minimum = a if a < b else b if b < c else c

print("minimum of", a, "and", b, "and", c, "is", minimum)

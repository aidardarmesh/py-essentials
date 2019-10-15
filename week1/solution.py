import sys

number_string = sys.argv[1]

print(sum([int(digit) for digit in number_string]))

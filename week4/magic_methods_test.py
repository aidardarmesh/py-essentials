from magic_methods import File

first = File('first')
first.write('first\n')

second = File('second')
second.write('second\n')

third = first + second
lines = []

for line in third:
    lines.append(line)

print(lines)
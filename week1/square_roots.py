import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d_root = (b**2 - 4*a*c)**0.5

x1 = (-b - d_root) / (2*a)
x2 = (-b + d_root) / (2*a)

print(int(x1))
print(int(x2))

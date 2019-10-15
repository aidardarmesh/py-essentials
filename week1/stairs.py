import sys

stairs_level = int(sys.argv[1])

for i in range(1 , stairs_level+1):
    print(" "*(stairs_level-i) + "#"*i)


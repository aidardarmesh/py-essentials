import os.path, tempfile

class File:
    """Интерфейс для работы с файлами"""

    def __init__(self, file_path):
        self.file_path = file_path
    
    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)
    
    def __add__(self, obj):
        

    def __str__(self):
        return self.file_path
    
    def __iter__(self):
        return open(self.file_path, 'r')

    def __next__(self):
        line = self.readline()

        if not line:
            self.close()
            print('I closed file')
            raise StopIteration
        
        return line

hello = File('hello.txt')
world = File('world.txt')

hello.write('hello\nmy\nfriend\n')
print(hello)

lines = []

for line in hello:
    lines.append(line)

print(lines)
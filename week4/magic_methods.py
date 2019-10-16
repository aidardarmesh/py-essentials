import os.path, tempfile

class File:
    """Интерфейс для работы с файлами"""

    def __init__(self, file_path):
        self.file_path = file_path
    
    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)
    
    def read(self):
        with open(self.file_path) as f:
            return f.read()
    
    def __add__(self, obj):
        dir = tempfile.gettempdir()
        file_name = '-'.join([self.file_path, obj.file_path])
        new_file_path = '/'.join([dir, file_name])
        new_obj = File(new_file_path)
        new_obj.write(self.read() + obj.read())

        return new_obj

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

first = File('first')
first.write('first\n')

second = File('second')
second.write('second\n')

third = first + second

# hello.write('hello\nmy\nfriend\n')
# print(hello)

# lines = []

# for line in hello:
#     lines.append(line)

# print(lines)
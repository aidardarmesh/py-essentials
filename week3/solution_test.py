from solution import FileReader

reader = FileReader('file/not/found/')
print(reader.read())
reader = FileReader('../week2/storage.py')
print(reader.read())

class FileReader:
    def __init__(self, path):
        self.path = path
    
    def read(self):
        content = ""

        try:
            f = open(self.path, 'r')
            content = f.read()
            f.close()
        except IOError:
            pass
        
        return content
class Sample:
    def __setitem__(self, key, value):
        print("trying set {}: {}".format(key, value))
        super().__setitem__(self, key, value)
    
    def __getitem__(self, key):
        print("trying get {}".format(key))

s = Sample()
s['marko'] = 'polo'
s['marko']
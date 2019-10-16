class Value:
    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = int(value * (1 - obj.comission))

class Account:
    amount = Value()

    def __init__(self, comission):
        self.comission = comission
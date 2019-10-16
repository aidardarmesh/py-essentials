class Value:
    """Дескриптор баланса с учетом комиссии"""

    def __get__(self, obj, obj_type):
        return self.value
    
    def __set__(self, obj, value):
        self.value = int(value * (1 - obj.commission))

class Account:
    amount = Value()

    def __init__(self, comission):
        self.commission = commission
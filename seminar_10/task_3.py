class OddEvenSeparator:
    def __init__(self):
        self.some_list = []

    def add_number(self,number):
        self.some_list.append(number)
    
    def even(self):
        return list(filter(lambda x: not x % 2,self.some_list))
    def odd(self):
        return list(filter(lambda x: x % 2,self.some_list))
    
separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(2)
separator.add_number(3)
separator.add_number(4)
separator.add_number(5)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))




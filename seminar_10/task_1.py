class Balance:

    def __init__(self):
        self.r = 0
        self.l = 0

    def add_right(self,right):
        self.r += right

    def add_left(self,left):
        self.l += left

    def result(self):
        if self.r > self.l:
            print('R')
        elif self.l > self.r:
            print('L')
        elif self.l == self.r:
            print('=')

balance = Balance()
balance.add_right(10)
balance.add_left(10)
balance.result()
    





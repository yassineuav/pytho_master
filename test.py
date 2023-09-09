class test:
    def __init__(self, amount, times=10):
        self.amount = amount
        self.times = times
    
        for i in range(0, times):
            balance = "{:,}".format(self.amount)
            print(f"{i}  ${balance}")
            self.amount = self.amount * 2
            

double = test(100, 11)

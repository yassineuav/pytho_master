class test:
    
    def __init__(self, amount=100, times=10, percent=1.5):
        self.amount = amount
        self.amount_full = amount
        self.times = times
        self.percent = percent
        
        self.percentage = 100
        self.percentage_2 = 100
        print(f"times  balance 100%   50%")
        for i in range(0, times):
            # balance = "{:,}".format(self.amount)
            print(f"{i}   ${self.amount_full:,}  ${self.amount:,}  {self.percentage}%  {self.percentage_2}% ")
            self.amount = self.amount * 1.5
            self.amount_full = self.amount_full * 2
            self.percentage *= 2
            self.percentage_2 *= 1.5

double = test(amount=100, times=11, percent=2)

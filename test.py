class test:
    
    def __init__(self, amount=100, times=11, percent=1.5):
        self.amount = amount
        self.times = times
        self.percent = percent
        self.week = 1
        self.percentage = 100
        print(f"times  balance 100%")
        self.week  = 1
        for i in range(0, times):
            # balance = "{:,}".format(self.amount)
            if i in [1, 6, 11, 16]:
                print(f"week {self.week}")
                self.week += 1
            print(f"{i}    ${self.amount:,}  {self.percentage}% ")
            self.amount = self.amount * 2
            self.percentage *= 2
            
    def __str__(self):
        return f"{self.amount=}"    
    
double = test(amount=100, times=20, percent=2)

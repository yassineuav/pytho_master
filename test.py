class test:
    def __init__(self, amount=100, times=10, percent=1.5):
        self.amount = amount
        self.times = times
        self.percent = percent
    
        for i in range(0, times):
            # balance = "{:,}".format(self.amount)
            print(f"{i}  ${self.amount:,}")
            self.amount = self.amount * percent
            

# double = test(100, 11, 2)

class list_weekday:
    day_names = [         
        'Monday',         
        'Tuesday',         
        'Wednesday',         
        'Thursday',         
        'Friday',         
        'Saturday',
        'Sunday',    
    ]
    # import calendar  
    # day_names = list(calendar.day_name)
    print(day_names)

list_weekday



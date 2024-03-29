

class SavingPlan:
    name: str
    saving_month: int
    total_balance: float
    earned_interest: float
    topup: dict[str, float]
    
    def __init__(self, pname, month):
        self.saving_month = month
        self.name = pname
    
    def decide_monthly_add(self, contributors: list['Contributor'], topup: float = 0):
        add: float = 0.00
        if topup:
            add += topup
        for i in contributors:
            add += i.monthly_add
        return add
        
    def culc_grow(self):
        pass
    
    class Contributor:
        name: str
        monthly_add: float
        saved: float
        
        def __init__(self, name, saved):
            self.name = name
            self.saved  = saved
    
    class Account:
        name: str
        interest_rate: float
        interest_rate_limited: float
        limited_period: int
        balance: float
        earned_interest: float = 0.00
        bonus: float = 0.00
        
        def __init__(self, aname, balance):
            self.name = aname
            self.balance = balance
        
        def set_interest_rate(self, rate: float):
            return rate/100


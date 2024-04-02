
    
class Account:
    name: str
    balance: float
    monthly_add:float = 0.00
    interest_transfer: bool = False
    interest_transfer_tgt: str
    earned_interest: float = 0.00
    earned_bonus: float = 0.00
    interests: dict = {}
    interest_periodicity: str
    
    class Interest:
        balance_tier: float = 0
        rate: float = 0.0
        limited_period: int = 0
        
    class Bonus:
        rate: float = 0.00
        limit: float = 0.00
        frequency: int = 0
        fixed: float = 0.00
        fixed_frequency: int = 0
        
    
    def __init__(self, aname):
        self.name = aname
    
    def set_interest_rate(self, rate: float):
        return rate/100
    
class SimulateCondition:
    name:str
    accounts:list[Account]
    saving_month: int
    contribute_accounts: list[Account] = []
    
    def __init__(self, name:str):
        self.name = name

class Simulate(SimulateCondition):
    total_balance: float
    earned_interest: float
    
    def decide_monthly_add(self, contributors: list['Contributor'], topup: float = 0):
        add: float = 0.00
        if topup:
            add += topup
        for i in contributors:
            add += i.monthly_add
        return add
    
    class Contributor:
        name: str
        monthly_add: float
        saved: float
        
        def __init__(self, name, saved):
            self.name = name
            self.saved  = saved


# TODO class 名を整理して　利率・利率が与えられる上限額・特別金利・特別金利期間・に対応する
# 　　

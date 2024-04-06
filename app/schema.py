
    
class Account:
    name: str
    interest_rate: float
    interest_rate_limited: float
    limited_period: int = 0
    balance: float
    earned_interest: float = 0.00
    bonus_interest_rate: float = 0.00
    bonus_limit: float = 0.00
    bonus_fixed: float = 0.00
    bonus_frequency: int = 0
    monthly_add:float = 0.00
    interest_transfer: bool = False
    interest_transfer_tgt: str
    
    def __init__(self, aname, balance):
        self.name = aname
        self.balance = balance
    
    def set_interest_rate(self, rate: float):
        return rate/100
    
class SimulateCondition:
    name:str
    accounts:list[Account]
    saving_month: int
    
    def __init__(self, name:str, month:int):
        self.saving_month = month
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


# TODO ACCOUNT classに、金額上限の利率をつける　期間利率の名前を変える
#　streamlitで描写
# stream lit で複数入力の方法を探す while文でできるか？
# ISAaccount

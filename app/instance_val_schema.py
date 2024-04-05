from pydantic import BaseModel, Field
from typing import Optional

    
class Account():
    name: str
    balance: float = 0.00
    monthly_add:float = 0.00
    interest_transfer_tgt: Optional[str] = None
    interest_periodicity: str = 'Monthly'
    interests: list['Interest'] = []
    bonus: Optional['Bonus'] = None
    
    def __init__(self, name):
        self.name = name
        self.interests.append(list)
        
    def set_interests(self, list):

    class Interest():
        balance_tier: float = 0
        rate: float = 0.0
        limited_period: int = 0
        
        def set_interest(self,balance_tier,rate,limited_period):
            self.balance_tier = balance_tier
            self.rate = rate
            self.limited_period = limited_period
        
        def set_interest_rate(self, rate: float):
            return rate/100
        
    class Bonus():
        rate: float = 0.00
        limit: float = 0.00
        frequency: int = 0
        fixed: float = 0.00
        fixed_frequency: int = 0

class SimulateCondition():
    name:str
    accounts:list[Account] = []
    saving_month: int = 1
    
    def __init__(self, name:str):
        self.name = name

class Simulate(SimulateCondition):
    total_balance: float
    earned_interest: float
    earned_bonus: float = 0.00
    
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


# TODO classをループで使う方法を探す。ディクショナリにしてみる0

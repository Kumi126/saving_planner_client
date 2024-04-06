from pydantic import BaseModel, Field
from typing import Optional

class Interest(BaseModel):
    balance_tier: float = 0
    rate: float = 0.0
    limited_period: int = 0
    
    def set_interest_rate(self, rate: float):
        return rate/100
    
class Bonus(BaseModel):
    rate: float = 0.00
    limit: float = 0.00
    frequency: int = 0
    fixed: float = 0.00
    fixed_frequency: int = 0
    
    
class Account(BaseModel):
    name: str
    balance: float = 0.00
    monthly_add:float = 0.00
    interest_transfer_tgt: Optional[str] = None
    interests: list
    interest_periodicity: str = 'Monthly'
    bonus: Optional[Bonus] = None
    
    def __init__(self, name):
        super().__init__(name=name, interests=[],bonus=None)

class SimulateCondition(BaseModel):
    name:str = Field(max_length=20)
    accounts:list[Account] = []
    saving_month: int = 1
    
    # def __init__(self, name:str):
    #     self.name = name

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

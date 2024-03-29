
import os

CONTRIBUTOR1: str = str(os.environ.get('contributor1'))
CONTRIBUTOR2: str = str(os.environ.get('contributor2'))
PLAN1: str = str(os.environ.get('plan1'))
P1_INTRST_RATE:float = float(str(os.environ.get('plan1_interest_rate')))
P1_INTRST_RATE_LIMITED:float = float(str(os.environ.get('plan1_interest_rate_limited')))
CNTR1_MONTHLY_ADD:float = float(str(os.environ.get('ctb1_monthly_add')))
CNTR2_MONTHLY_ADD :float= float(str(os.environ.get('ctb2_monthly_add')))
CNTR1_SAVED:float = float(str(os.environ.get('ctb1_saved')))
CNTR2_SAVED:float = float(str(os.environ.get('ctb2_saved')))


class SavingPlanner:
    name: str
    saving_month: int
    total_balance: float
    earned_interest: float
    topup: dict[str, float]
    
    def __init__(self, pname, month):
        self.saving_month = month
        self.name = pname
    
    def decide_monthly_add(self, contributors: list['Contributor'], topup: float = 0):
        add = 0.00
        for i in contributors:
            add += i.monthly_add
        
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
        
        def __init__(self, aname, balance):
            self.name = aname
            self.balance = balance
        
        def set_interest_rate(self, rate: float):
            return rate/100

## continie the same saving method
def cal_plan():
    plan = SavingPlanner(PLAN1,13)
    usr1 = plan.Contributor(CONTRIBUTOR1, CNTR1_SAVED)
    usr2 = plan.Contributor(CONTRIBUTOR2, CNTR2_SAVED)
    usr1.monthly_add = CNTR1_MONTHLY_ADD
    usr2.monthly_add = CNTR2_MONTHLY_ADD
    monthly_add = plan.decide_monthly_add([usr1,usr2])
    ac1 = plan.Account('Esaver', usr2.saved + usr1.saved)
    ac1.interest_rate = ac1.set_interest_rate(1.19)
    ac1.interest_rate_limited = ac1.set_interest_rate(1.98)
    ac1.limited_period = 1
    
    count_month: int = 1
    while count_month <= plan.saving_month:
        if count_month <= ac1.limited_period:
            int_rate =  ac1.interest_rate_limited
        else:
            int_rate = ac1.interest_rate
        
        print(count_month)
        count_month += 1

def main():
    cal_plan()
    
if __name__ == '__main__':
    main()
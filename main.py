
import os
from app.schema import SavingPlan

CONTRIBUTOR1: str = str(os.environ.get('contributor1'))
CONTRIBUTOR2: str = str(os.environ.get('contributor2'))
PLAN1: str = str(os.environ.get('plan1'))
AC1_NAME:str = str(os.environ.get('account1'))
AC2_NAME:str = str(os.environ.get('account2'))
AC3_NAME:str = str(os.environ.get('account3'))
AC4_NAME:str = str(os.environ.get('account4'))
AC5_NAME:str = str(os.environ.get('account5'))
AC1_INTRST_RATE:float = float(str(os.environ.get('ac1_interest_rate')))
AC1_INTRST_RATE_LIMITED:float = float(str(os.environ.get('ac1_interest_rate_limited')))
AC2_INTRST_RATE:float = float(str(os.environ.get('ac2_interest_rate')))
AC2_INTRST_RATE_LIMITED:float = float(str(os.environ.get('ac2_interest_rate_limited')))
AC3_INTRST_RATE:float = float(str(os.environ.get('ac3_interest_rate')))
AC3_INTRST_RATE_LIMITED:float = float(str(os.environ.get('ac3_interest_rate_limited')))
AC4_INTRST_RATE:float = float(str(os.environ.get('ac4_interest_rate')))
AC4_BONUS:float = float(str(os.environ.get('ac4_bonus_interest_rate')))
AC4_BONUS_FREQUENCY:int = int(str(os.environ.get('ac4_bonus_frequency')))
AC4_BONUS_LIMIT: float = float(str(os.environ.get('ac4_bonus_limit')))
AC5_INTRST_RATE:float = float(str(os.environ.get('ac5_interest_rate')))
AC5_BONUS:float = float(str(os.environ.get('ac5_bonus_interest_rate')))
AC5_BONUS_FREQUENCY:int = int(str(os.environ.get('ac5_bonus_frequency')))
AC5_BONUS_LIMIT: float = float(str(os.environ.get('ac5_bonus_limit')))
CNTR1_MONTHLY_ADD:float = float(str(os.environ.get('ctb1_monthly_add')))
CNTR2_MONTHLY_ADD :float= float(str(os.environ.get('ctb2_monthly_add')))
CNTR1_SAVED:float = float(str(os.environ.get('ctb1_saved')))
CNTR2_SAVED:float = float(str(os.environ.get('ctb2_saved')))

## input condition

def cal_plan():
    plan = SavingPlan(PLAN1,13)
    
    users:list[SavingPlan.Contributor] = []
    users.append(usr1:= plan.Contributor(CONTRIBUTOR1, CNTR1_SAVED))
    users.append(usr2:= plan.Contributor(CONTRIBUTOR2, CNTR2_SAVED))
    
    users[0].monthly_add = CNTR1_MONTHLY_ADD
    users[1].monthly_add = CNTR2_MONTHLY_ADD
    adding = plan.decide_monthly_add(users)

    
    accounts:list[SavingPlan.Account] = []
    accounts.append(ac1:= plan.Account(AC1_NAME, 100))
    accounts.append(ac2:= plan.Account(AC2_NAME, 4000))
    accounts.append(ac3:= plan.Account(AC3_NAME, 4000))
    accounts.append(ac4:= plan.Account(AC4_NAME, 1))
    accounts.append(ac5:= plan.Account(AC5_NAME, 1))
    accounts[0].interest_rate = accounts[0].set_interest_rate(AC1_INTRST_RATE)
    accounts[0].interest_rate_limited = accounts[0].set_interest_rate(AC1_INTRST_RATE_LIMITED) 
    accounts[1].interest_rate = accounts[1].set_interest_rate(AC2_INTRST_RATE)
    accounts[1].interest_rate_limited = accounts[1].set_interest_rate(AC2_INTRST_RATE_LIMITED) 
    accounts[2].interest_rate = accounts[2].set_interest_rate(AC3_INTRST_RATE)
    accounts[2].interest_rate_limited = accounts[2].set_interest_rate(AC3_INTRST_RATE_LIMITED) 
    accounts[3].interest_rate = accounts[3].set_interest_rate(AC4_INTRST_RATE) 
    accounts[4].interest_rate = accounts[4].set_interest_rate(AC5_INTRST_RATE) 
    
    
    accounts[3].bonus_interest_rate = accounts[3].set_interest_rate(AC4_BONUS)
    accounts[4].bonus_interest_rate = accounts[4].set_interest_rate(AC5_BONUS)
    accounts[3].bonus_limit = AC4_BONUS_LIMIT
    accounts[4].bonus_limit = AC5_BONUS_LIMIT
    accounts[3].bonus_frequency = AC4_BONUS_FREQUENCY
    accounts[4].bonus_frequency = AC5_BONUS_FREQUENCY
    
    accounts[1].interest_transfer = True
    accounts[1].interest_transfer_tgt = 'esaver'
    accounts[2].interest_transfer = True
    accounts[2].interest_transfer_tgt = 'esaver'
    
    account_names = [account.name for account in accounts]
    if accounts[1].interest_transfer_tgt in account_names:
        pass
    else:
        print('There is no match target bank acount name')
    
    accounts[0].monthly_add = 84
    accounts[1].monthly_add = 0
    accounts[2].monthly_add = 0
    accounts[3].monthly_add = 333
    accounts[4].monthly_add = 333
    
    
    ac1.limited_period = 1 ##
    ac2.limited_period = 1 ##
    ac3.limited_period = 3 ##
  
    count_month: int = 1
    while count_month <= plan.saving_month:
        print(count_month,'month')
        interest_transfer_pool:dict[str, float] = {}
        for acnt in accounts:
            print(acnt.name)
            # if interest rate will be changed after ac1.limited_period month
            if count_month <= acnt.limited_period:
                int_rate =  acnt.interest_rate_limited
            else:
                int_rate = acnt.interest_rate
            adding_interest:float = ((acnt.balance + acnt.monthly_add)*int_rate)/12
            print(adding_interest)
            # For the case interest will be added another account everymonth
            # interest transfer will be added after all acounts interest culculated,
            # current month transfered interest will not affect on current month adding interest of target account 
            if acnt.interest_transfer and acnt.interest_transfer_tgt:
                tgt:str = acnt.interest_transfer_tgt
                pool:float
                if tgt in interest_transfer_pool.keys():
                    pool = interest_transfer_pool[tgt]
                else:
                    pool = 0.00
                
                interest_transfer_pool[tgt] = pool + adding_interest
                new_balance = acnt.balance + acnt.monthly_add
            else:
                new_balance = acnt.balance + acnt.monthly_add + adding_interest
            
            # if bonus apply
            if acnt.bonus_interest_rate and count_month%acnt.bonus_frequency == 0:
                bonus_amount = new_balance*acnt.bonus_interest_rate
                if bonus_amount > acnt.bonus_limit:
                    bonus_amount = acnt.bonus_limit
                adding_interest += bonus_amount
                new_balance += bonus_amount
                
            elif acnt.bonus_fixed and count_month%acnt.bonus_frequency == 0:
                new_balance += acnt.bonus_fixed
            
            # update added amount
            acnt.earned_interest += adding_interest
            acnt.balance = new_balance
            
        print(interest_transfer_pool)
        
        for tgt, transferd_intrest in interest_transfer_pool.items():
            for account in accounts:
                if tgt == account.name:
                    account.balance += transferd_intrest
                    
        
        count_month += 1
    balances:list[float] = [acnt.balance for acnt in accounts]
    earned_interests:list[float] = [acnt.earned_interest for acnt in accounts]
    plan.total_balance = sum(balances)
    plan.earned_interest = sum(earned_interests)
    
    print(f'''
          TOTAL BALANCE:{plan.total_balance}
          EARNED INTERST:{plan.earned_interest}
    ''')

def main():
    cal_plan()
    
if __name__ == '__main__':
    main()
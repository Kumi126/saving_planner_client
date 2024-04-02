import streamlit as st
from app.new_schema import SimulateCondition,Account


def add_accounts():
    count = 1
    intr_c = 1
    bns_c = 0

    def add_account(count):
        
        def add_interest(intr_c,link_account:Account):
            __ = link_account.Interest()
            col1_1, col1_2, col1_3 = st.columns(3)
            with col1_1:
                __.balance_tier = st.number_input(key=f'balance_tier_{intr_c}', label='Balance tires')
            with col1_2:
                __.rate = st.number_input(key=f'rate_{intr_c}', label='Interest rate')
            with col1_3:
                __.limited_period = int(st.number_input(key=f'limited_period_{intr_c}', label='For How many month?'))
            
            key = str(intr_c - 1)
            link_account.interests['%s' %key] = {
                'tier': __.balance_tier,
                'rate': __.rate,
                'limited_period': __.limited_period
            }
            
            if intr_c <= max_interest_condition:
                more_intr = st.toggle(key=f'interest_toggle_{intr_c}',label=f'Add more interest conditions')
                if more_intr:
                    intr_c += 1
                    add_interest(intr_c,link_account)
        
        st.write('#### Accounts')            
        _ = Account(st.text_input(key=f'account_{count}', label=f'Account name{count}'))
        _.balance = st.number_input(key=f'balance_{count}', label='Account balance')
        _.monthly_add = st.number_input(key=f'monthly_add_{count}', label='How much will you pay in each month?')
        
        st.write('##### Tell about interest')
        add_interest(intr_c,_)

        bonus = st.toggle(key=f'bonus_toggle_{count}', label=f'Does this account have any periodical bonus? Or will you plan to tap up extra money occacionally?')
        if bonus:
            col2_1, col2_2 = st.columns(2)
            with col2_1:
                _.Bonus.fixed = st.number_input(key=f'bonus_fixed_{count}', label='Fix bonus amount.')
            with col2_2:
                _.Bonus.fixed_frequency = int(st.number_input(key=f'bonus_fixed_frequency_{count}', label='How often? (once in XX monthes)'))
            col3_1, col3_2, col3_3 = st.columns(3)
            with col3_1:
                _.Bonus.rate = st.number_input(key=f'bonus_rate_{count}', label='Bonus rate')
            with col3_2:
                _.Bonus.limit = st.number_input(key=f'bonus_limit_{count}', label='Max amount of bonus')
            with col3_3:
                _.Bonus.frequency = int(st.number_input(key=f'bonus_frequency_{count}', label='How often? (once in XX monthes)'))

        accounts.append(_)
        if count < max_accounts:
            add_more = st.toggle(key=f'tg_{count}',label=f'Add more contribute account')
            
            if add_more:
                count += 1
                add_account(count)
        else:
            pass

    add_account(count)
    

simu: SimulateCondition 
max_accounts = 8
max_interest_condition = 3

st.write('### Mulitopult account saving simulattor')
simu = SimulateCondition(st.text_input(key='simulate_name', label=f'Name this simulation', max_chars=20))
simu.saving_month = int(st.number_input('How long will you save (months)?',min_value=1,step=1))
accounts:list[Account] = []
add_accounts()


st.write(simu)
for i in accounts:
    st.write('account obj')
    st.write(i)
    st.write('interest list')
    st.write(i.interests)
    st.write('interest')
    st.write(i.Interest.rate)
    st.write('bonus fixed amount')
    st.write(i.Bonus.fixed)
st.write('number of accounts')
st.write(len(accounts))



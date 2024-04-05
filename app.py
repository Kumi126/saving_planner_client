import streamlit as st
from app.new_schema import SimulateCondition,Account,Interest,Bonus


def add_accounts():

    count = 1
    intr_c = 1
    accounts:list[Account] = []
    def add_account(count,intr_c):
        interests = []
        def add_interest(intr_c,link_account:Account):
            st.write(intr_c)
            interest = Interest()
            col2_1, col2_2, col2_3 = st.columns(3)
            with col2_1:
                interest.balance_tier = st.number_input(key=f'balance_tier_{intr_c}', label='Balance tires')
            with col2_2:
                interest.rate = st.number_input(key=f'rate_{intr_c}', label='Interest rate')
            with col2_3:
                interest.limited_period = int(st.number_input(key=f'limited_period_{intr_c}', label='For How many month?'))
            
            interests.append(interest)
            if len(interests) < max_interest_condition:
                more_intr = st.toggle(key=f'interest_toggle_{intr_c}',label=f'Add more interest conditions')
                if more_intr:
                    intr_c += 1
                    add_interest(intr_c,link_account)

        col1_1, col1_2, col1_3 = st.columns(3)
        with col1_1:
            acc_name = st.text_input(key=f'account_{count}', label=f'Account name{count}')
            acc = Account(name=acc_name)
        with col1_2:     
            acc.balance = st.number_input(key=f'balance_{count}', label='Account balance')
        with col1_3:     
            acc.monthly_add = st.number_input(key=f'monthly_add_{count}', label='Monthly adding amount')
        
        st.write('##### Tell about interest')
        acc.interest_periodicity = str(st.radio(key=f'perid_{count}',label='Recieve interest', options=['Monthly', 'Annually']))
        add_interest(intr_c,acc)
        acc.interests = interests

        bonus = st.toggle(key=f'bonus_toggle_{count}', label=f'Does this account have any periodical bonus? Or will you plan to tap up extra money occacionally?')
        if bonus:
            bns = Bonus()
            col3_1, col3_2 = st.columns(2)
            with col3_1:
                bns.fixed = st.number_input(key=f'bonus_fixed_{count}', label='Fix bonus amount.')
            with col3_2:
                bns.fixed_frequency = int(st.number_input(key=f'bonus_fixed_frequency_{count}', label='How often? (once in XX monthes)'))
            col4_1, col4_2, col4_3 = st.columns(3)
            with col4_1:
                bns.rate = st.number_input(key=f'bonus_rate_{count}', label='Bonus rate')
            with col4_2:
                bns.limit = st.number_input(key=f'bonus_limit_{count}', label='Max amount of bonus')
            with col4_3:
                bns.frequency = int(st.number_input(key=f'bonus_frequency_{count}', label='How often? (once in XX monthes)'))

            acc.bonus = bns
        if count < max_accounts:
            add_more = st.toggle(key=f'tg_{count}',label=f'Add more contribute account')
            accounts.append(acc)
            
            if add_more:
                count += 1
                intr_c += 100
                add_account(count,intr_c)
        else:
            pass

    add_account(count,intr_c)
    return accounts

# simu: SimulateCondition 
max_accounts = 8
max_interest_condition = 3

st.write('### Mulitipul account saving simulator')
simu_name = st.text_input(key='simulate_name', label=f'Name this simulation', max_chars=20)
simu = SimulateCondition(name=simu_name)
col0_1, col0_2, col0_3= st.columns(3)
with col0_1:
    saving_year = st.text_input(key='saving_y',label='How long will you save?',max_chars=2,placeholder='year(s)')
with col0_2:
    saving_month = st.text_input(key='saving_m',label='month(s)',max_chars=2,placeholder='month(s)')

if (saving_year and saving_month):
    try:
        saving_year = int(saving_year)
        saving_month = int(saving_month)
        simu.saving_month = (12*saving_month) + saving_month
    except Exception:
    
        st.error('Please put number of month/year')
st.write('#### Accounts')
accounts = add_accounts()
conditon_submit_button = st.button(key='button_1', label='Submit condition')
# if conditon_submit_button:
#     simu.accounts = accounts
with st.form('submit simulation'):
    st.write('### ')
    st.write(f'Simulation name: {simu.name}')
    st.write(f'Contribute accounts:')
    for i in accounts:
        st.write(f'- {i.name}')
    st.write('number of accounts')
    st.write(len(accounts))
    st.write('Bonus')
    if i.bonus:
        st.write(f'{i.bonus.fixed}')
    submit_button = st.form_submit_button(label='simulate')

for i in accounts:
    print(f'- {i.name}')
    
